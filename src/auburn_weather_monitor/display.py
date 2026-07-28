from pathlib import Path


def print_summary(
    records: list[dict[str, object]],
    raw_path: Path,
    processed_path: Path,
    forecast_url: str,
) -> None:
    print("Auburn weather monitor")
    print(f"Forecast URL: {forecast_url}")
    print(f"Raw output: {raw_path}")
    print(f"Processed output: {processed_path}")
    print(f"Forecast periods: {len(records)}")

    if records:
        first = records[0]
        print("First period:")
        print(f"- Name: {first['name']}")
        print(f"- Temperature: {first['temperature']} {first['temperature_unit']}")
        print(f"- Forecast: {first['short_forecast']}")


def print_project_info(user_agent: str) -> None:
    configured = user_agent != "auburn-weather-monitor/0.1 (contact email not configured)"
    print("Auburn weather monitor project info")
    print("Package: auburn-weather-monitor")
    print("API: National Weather Service API")
    print("Default location: Auburn, Alabama")
    print(f"NWS_USER_AGENT configured: {configured}")
    print("Raw output path: data/raw/forecast.json")
    print("Processed output path: data/processed/forecast_periods.csv")
