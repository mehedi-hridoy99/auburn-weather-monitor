import json
import logging
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from pydantic import ValidationError

from auburn_weather_monitor.models import ForecastResponse, PointResponse


NWS_BASE_URL = "https://api.weather.gov"
logger = logging.getLogger(__name__)


class ApiError(RuntimeError):
    """Raised when the weather API request cannot be completed."""


def fetch_json(url: str, user_agent: str, timeout: int = 30) -> dict:
    logger.debug("Requesting %s", url)
    request = Request(
        url,
        headers={
            "Accept": "application/geo+json, application/json",
            "User-Agent": user_agent,
        },
    )
    try:
        with urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        raise ApiError(f"API request failed with HTTP {error.code}: {url}") from error
    except URLError as error:
        raise ApiError(f"API request failed: {error.reason}") from error
    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        raise ApiError(f"API returned invalid JSON: {url}") from error


def fetch_forecast(latitude: float, longitude: float, user_agent: str) -> dict:
    point_url = f"{NWS_BASE_URL}/points/{latitude:.4f},{longitude:.4f}"
    point_data = fetch_json(point_url, user_agent)
    try:
        point = PointResponse.model_validate(point_data)
    except ValidationError as error:
        raise ApiError(f"Point response validation failed: {error}") from error

    forecast_url = point.properties.forecast
    forecast_data = fetch_json(forecast_url, user_agent)
    try:
        ForecastResponse.model_validate(forecast_data)
    except ValidationError as error:
        raise ApiError(f"Forecast response validation failed: {error}") from error

    return {
        "point_url": point_url,
        "forecast_url": forecast_url,
        "point": point_data,
        "forecast": forecast_data,
    }
