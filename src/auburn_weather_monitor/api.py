import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


NWS_BASE_URL = "https://api.weather.gov"


class ApiError(RuntimeError):
    """Raised when the weather API request cannot be completed."""


def fetch_json(url: str, user_agent: str, timeout: int = 30) -> dict:
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


def fetch_forecast(latitude: float, longitude: float, user_agent: str) -> dict:
    point_url = f"{NWS_BASE_URL}/points/{latitude:.4f},{longitude:.4f}"
    point_data = fetch_json(point_url, user_agent)
    forecast_url = point_data["properties"]["forecast"]
    forecast_data = fetch_json(forecast_url, user_agent)
    return {
        "point_url": point_url,
        "forecast_url": forecast_url,
        "point": point_data,
        "forecast": forecast_data,
    }
