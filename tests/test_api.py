import json
from pathlib import Path
from urllib.error import URLError

import pytest

from auburn_weather_monitor import api
from auburn_weather_monitor.api import ApiError


FIXTURES = Path(__file__).parent / "fixtures"


def load_fixture(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def test_fetch_forecast_uses_controlled_responses(monkeypatch):
    point = load_fixture("point.json")
    forecast = load_fixture("forecast.json")
    responses = iter([point, forecast])

    monkeypatch.setattr(api, "fetch_json", lambda *args, **kwargs: next(responses))

    result = api.fetch_forecast(32.6099, -85.4808, "test-agent")

    assert result["forecast_url"] == point["properties"]["forecast"]
    assert result["forecast"] == forecast


def test_fetch_json_wraps_connection_failure(monkeypatch):
    def fail(*args, **kwargs):
        raise URLError("offline")

    monkeypatch.setattr(api, "urlopen", fail)

    with pytest.raises(ApiError, match="offline"):
        api.fetch_json("https://example.invalid", "test-agent")


def test_fetch_forecast_rejects_invalid_incoming_data(monkeypatch):
    monkeypatch.setattr(
        api,
        "fetch_json",
        lambda *args, **kwargs: {"properties": {}},
    )

    with pytest.raises(ApiError, match="validation failed"):
        api.fetch_forecast(32.6099, -85.4808, "test-agent")
