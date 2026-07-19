# Auburn Weather Monitor

## Overview

This project is a small command-line tool for Practicum 4. It calls the National Weather Service API for a forecast near Auburn, Alabama, saves the raw API response, and creates a processed CSV file that is easier to inspect.

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
- Internet access

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

The default outputs are:

```text
data/raw/forecast.json
data/processed/forecast_periods.csv
```

Use a different location:

```bash
uv run auburn-weather-monitor --latitude 32.6099 --longitude -85.4808
```

## How to Test

```bash
uv run python -m pytest
```

## Project Structure

```text
src/auburn_weather_monitor/
  api.py          API request boundary
  cli.py          command-line interface
  config.py       local .env loading
  display.py      terminal output
  output.py       raw JSON and processed CSV writers
  processing.py   forecast record extraction
tests/
  test_processing.py
data/
  raw/            generated raw API evidence, ignored by Git
  processed/      generated processed CSV, ignored by Git
```

## Notes

- `.env`, `.venv/`, and `data/` are ignored by Git.
- `.env.example` is committed so another person can recreate the local configuration.
- The project uses the Python standard library only.

## Known Issues

- The National Weather Service API can fail if there is no internet connection or if the service is temporarily unavailable.
- The first version only processes the forecast periods returned by the API. It does not yet validate weather alerts or compare multiple locations.
