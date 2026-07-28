from auburn_weather_monitor.models import ForecastResponse


def forecast_periods(raw_response: dict) -> list[dict[str, object]]:
    periods = raw_response["forecast"]["properties"].get("periods", [])
    validated = ForecastResponse.model_validate({"properties": {"periods": periods}})
    records: list[dict[str, object]] = []

    for period in validated.properties.periods:
        records.append(
            {
                "number": period.number,
                "name": period.name,
                "start_time": period.startTime,
                "end_time": period.endTime,
                "temperature": period.temperature,
                "temperature_unit": period.temperatureUnit,
                "wind_speed": period.windSpeed,
                "wind_direction": period.windDirection,
                "short_forecast": period.shortForecast,
            }
        )

    return records
