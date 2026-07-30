"""Tests for reusable report loading and analysis."""

import json

import pytest

from auburn_weather_monitor.reporting import (
    load_forecast_records,
    temperature_summary,
)


def test_load_forecast_records_uses_project_processing(tmp_path):
    raw = {
        "forecast": {
            "properties": {
                "periods": [
                    {
                        "number": 1,
                        "name": "Tonight",
                        "startTime": "2026-07-30T18:00:00-05:00",
                        "endTime": "2026-07-31T06:00:00-05:00",
                        "temperature": 72,
                        "temperatureUnit": "F",
                        "windSpeed": "0 mph",
                        "windDirection": "",
                        "shortForecast": "Clear",
                    }
                ]
            }
        }
    }
    path = tmp_path / "forecast.json"
    path.write_text(json.dumps(raw), encoding="utf-8")

    records = load_forecast_records(path)

    assert records[0]["name"] == "Tonight"
    assert records[0]["temperature"] == 72


def test_temperature_summary_reports_range_and_average():
    records = [
        {"name": "Tonight", "temperature": 70, "temperature_unit": "F"},
        {"name": "Friday", "temperature": 90, "temperature_unit": "F"},
    ]

    summary = temperature_summary(records)

    assert summary["average"] == 80
    assert summary["highest_period"] == "Friday"
    assert summary["lowest_period"] == "Tonight"


def test_temperature_summary_rejects_mixed_units():
    records = [
        {"name": "One", "temperature": 70, "temperature_unit": "F"},
        {"name": "Two", "temperature": 20, "temperature_unit": "C"},
    ]

    with pytest.raises(ValueError, match="one consistent unit"):
        temperature_summary(records)
