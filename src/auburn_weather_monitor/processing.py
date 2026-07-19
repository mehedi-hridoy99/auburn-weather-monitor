def forecast_periods(raw_response: dict) -> list[dict[str, str]]:
    periods = raw_response["forecast"]["properties"].get("periods", [])
    records: list[dict[str, str]] = []

    for period in periods:
        records.append(
            {
                "number": period.get("number", ""),
                "name": period.get("name", ""),
                "start_time": period.get("startTime", ""),
                "end_time": period.get("endTime", ""),
                "temperature": period.get("temperature", ""),
                "temperature_unit": period.get("temperatureUnit", ""),
                "wind_speed": period.get("windSpeed", ""),
                "wind_direction": period.get("windDirection", ""),
                "short_forecast": period.get("shortForecast", ""),
            }
        )

    return records
