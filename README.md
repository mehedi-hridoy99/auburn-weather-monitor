# Auburn Weather Monitor

## Overview

This project is a command-line tool and Streamlit dashboard for an Auburn weather forecast. It calls the National Weather Service API, validates incoming data with Pydantic, saves the raw response, and creates a processed CSV file.

## API

API: National Weather Service API

Documentation: https://www.weather.gov/documentation/services-web-api

Example request:

```text
https://api.weather.gov/points/32.6099,-85.4808
```

That request returns metadata for the requested latitude and longitude, including a forecast URL. The project then calls the forecast URL and extracts forecast periods with fields such as period name, start time, temperature, wind speed, and short forecast.

One line on what I will build: I will build a small weather-monitoring project that collects forecast data for Auburn and turns it into inspectable records for later analysis or reporting.

## Requirements

- Python 3.11 or newer
- `uv`
- Internet access for live forecasts

## Setup

Create a local `.env` file from the example:

```bash
cp .env.example .env
```

Edit `.env` and replace the placeholder email in `NWS_USER_AGENT` with your contact email. The National Weather Service asks API users to send a clear user agent.

## How to Run

Show setup information without calling the API:

```bash
uv run auburn-weather-monitor --project-info
```

Fetch the Auburn forecast and save outputs:

```bash
uv run auburn-weather-monitor
```

Write logs to the console and a file:

```bash
uv run auburn-weather-monitor --log-level INFO --log-file logs/weather.log
```

The default outputs are:

```text
data/raw/forecast.json
data/processed/forecast_periods.csv
```

Use a different location:

```bash
uv run auburn-weather-monitor --latitude 32.6099 --longitude -85.4808
```

## Dashboard

Start the local Streamlit dashboard:

```bash
uv run streamlit run src/auburn_weather_monitor/dashboard.py
```

Open the local URL shown by Streamlit. Select a latitude and longitude, then choose **Load forecast**. Deployment is not required.

## How to Test

```bash
uv run python -m pytest
```

The tests use committed JSON fixtures and mocks. They do not contact the live National Weather Service API.

## Project Structure

```text
src/auburn_weather_monitor/
  api.py          API request boundary
  cli.py          command-line interface
  config.py       local .env loading
  dashboard.py    Streamlit interface
  display.py      terminal output
  logging_config.py console and file logging setup
  models.py       Pydantic runtime validation models
  output.py       raw JSON and processed CSV writers
  processing.py   forecast record extraction
  service.py      shared CLI and dashboard workflow
tests/
  fixtures/       committed API response samples
  test_api.py
  test_logging.py
  test_processing.py
data/
  raw/            generated raw API evidence, ignored by Git
  processed/      generated processed CSV, ignored by Git
```

## Notes

- `.env`, `.venv/`, and `data/` are ignored by Git.
- `.env.example` is committed so another person can recreate the local configuration.
- The CLI and dashboard use the same service and processing logic.
- Pydantic produces a clear validation error when required API fields are missing or invalid.
- Logs do not include the local user-agent value or other configuration secrets.

## Known Issues

- The National Weather Service API can fail if there is no internet connection or if the service is temporarily unavailable.
- The first version only processes the forecast periods returned by the API. It does not yet validate weather alerts or compare multiple locations.
