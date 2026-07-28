import logging

from auburn_weather_monitor.api import fetch_forecast
from auburn_weather_monitor.processing import forecast_periods


logger = logging.getLogger(__name__)


def get_forecast(
    latitude: float,
    longitude: float,
    user_agent: str,
) -> tuple[dict, list[dict[str, object]]]:
    logger.info("Requesting forecast for latitude %.4f, longitude %.4f", latitude, longitude)
    raw_response = fetch_forecast(latitude, longitude, user_agent)
    records = forecast_periods(raw_response)
    logger.info("Validated and processed %d forecast periods", len(records))
    return raw_response, records
