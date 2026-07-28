import logging

from auburn_weather_monitor.logging_config import configure_logging


def test_configure_logging_writes_to_file(tmp_path):
    log_path = tmp_path / "weather.log"
    configure_logging("INFO", log_path)

    logging.getLogger("test").info("fixture test message")

    assert "fixture test message" in log_path.read_text(encoding="utf-8")
