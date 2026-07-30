"""Load validated project data and calculate report summaries."""

import json
from pathlib import Path

from auburn_weather_monitor.processing import forecast_periods


def load_forecast_records(path: Path) -> list[dict[str, object]]:
    """Load raw project JSON and return validated, processed forecast records."""
    raw_response = json.loads(path.read_text(encoding="utf-8"))
    return forecast_periods(raw_response)


def temperature_summary(records: list[dict[str, object]]) -> dict[str, object]:
    """Summarize the range and average of same-unit forecast temperatures.

    Raises:
        ValueError: If no records are provided or temperature units differ.
    """
    if not records:
        raise ValueError("At least one forecast record is required.")

    units = {str(record["temperature_unit"]) for record in records}
    if len(units) != 1:
        raise ValueError("Temperature records must use one consistent unit.")

    temperatures = [float(record["temperature"]) for record in records]
    highest_index = temperatures.index(max(temperatures))
    lowest_index = temperatures.index(min(temperatures))
    return {
        "period_count": len(records),
        "unit": units.pop(),
        "average": sum(temperatures) / len(temperatures),
        "highest": max(temperatures),
        "highest_period": records[highest_index]["name"],
        "lowest": min(temperatures),
        "lowest_period": records[lowest_index]["name"],
    }
