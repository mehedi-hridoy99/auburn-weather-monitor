from auburn_weather_monitor.processing import forecast_periods


def test_forecast_periods_extracts_expected_fields():
    raw = {
        "forecast": {
            "properties": {
                "periods": [
                    {
                        "number": 1,
                        "name": "Tonight",
                        "startTime": "2026-07-18T18:00:00-05:00",
                        "endTime": "2026-07-19T06:00:00-05:00",
                        "temperature": 72,
                        "temperatureUnit": "F",
                        "windSpeed": "5 mph",
                        "windDirection": "S",
                        "shortForecast": "Partly Cloudy",
                    }
                ]
            }
        }
    }

    records = forecast_periods(raw)

    assert records == [
        {
            "number": 1,
            "name": "Tonight",
            "start_time": "2026-07-18T18:00:00-05:00",
            "end_time": "2026-07-19T06:00:00-05:00",
            "temperature": 72,
            "temperature_unit": "F",
            "wind_speed": "5 mph",
            "wind_direction": "S",
            "short_forecast": "Partly Cloudy",
        }
    ]
