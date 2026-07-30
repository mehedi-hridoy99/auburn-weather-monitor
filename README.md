# Auburn Weather Monitor

Auburn Weather Monitor retrieves a National Weather Service forecast for Auburn,
Alabama, validates the response, and creates JSON and CSV outputs. It provides a
command-line interface for repeatable data collection and a local Streamlit
dashboard for quick inspection. The project is intended for students and
analysts who want a small, reproducible example of an API-backed Python project.

## Fastest Path

Requirements:

- Python 3.11 or newer
- [`uv`](https://docs.astral.sh/uv/)
- Internet access when requesting a new forecast

Restore the environment, create local configuration, and run the project:

```bash
uv sync
cp .env.example .env
uv run auburn-weather-monitor
```

On Windows PowerShell, copy the configuration file with:

```powershell
Copy-Item .env.example .env
```

The run writes:

- `data/raw/forecast.json`: the complete point and forecast API responses
- `data/processed/forecast_periods.csv`: one row per forecast period

A committed example of both outputs is included so the project and report can
be inspected without contacting the API.

## Configuration

The only supported environment variable is:

| Variable | Required | Purpose |
|---|---:|---|
| `NWS_USER_AGENT` | Recommended | Identifies the client to the National Weather Service. Use an application name and contact email. |

Create `.env` from `.env.example`, then replace the placeholder address:

```text
NWS_USER_AGENT=auburn-weather-monitor/0.1 (mailto:your-email@example.com)
```

Never commit `.env` or a private contact address. The application uses a clear
placeholder user agent when this variable is not configured.

## Command-Line Usage

Show all options:

```bash
uv run auburn-weather-monitor --help
```

Fetch the default Auburn forecast:

```bash
uv run auburn-weather-monitor
```

Choose another location:

```bash
uv run auburn-weather-monitor --latitude 32.6099 --longitude -85.4808
```

Write INFO-level logs to the console and a file:

```bash
uv run auburn-weather-monitor --log-level INFO --log-file logs/weather.log
```

Show configuration and output paths without calling the API:

```bash
uv run auburn-weather-monitor --project-info
```

## Dashboard

Start the local dashboard:

```bash
uv run streamlit run src/auburn_weather_monitor/dashboard.py
```

Open the local URL printed by Streamlit. Confirm or change the coordinates and
select **Load forecast**. If a request fails, the dashboard displays the API or
validation error so the user can retry or check the configuration.

## Reproducible Report

The report asks how temperatures change across the available Auburn forecast
periods. It uses the committed raw response and calls the project's validation
and processing code.

- [Report source](reports/auburn-forecast-report.qmd)
- [Rendered PDF](reports/auburn-forecast-report.pdf)
- [Data dictionary](docs/data-dictionary.md)

After restoring the project environment and installing Quarto, rebuild it from
the repository root:

```bash
quarto render reports/auburn-forecast-report.qmd
```

Do not edit the rendered PDF directly. Update the `.qmd`, code, or input data
and render again.

## Testing

Run the automated tests:

```bash
uv run python -m pytest
```

The tests use committed fixtures and controlled mocks. They do not contact the
live National Weather Service API.

## Inputs and Outputs

The default input is the National Weather Service points endpoint for latitude
`32.6099` and longitude `-85.4808`. That response supplies the forecast URL.
Pydantic validates required point, forecast, and period fields before processing.

The raw JSON preserves API evidence. The processed CSV contains the fields
described in the [data dictionary](docs/data-dictionary.md).

## Project Structure

```text
src/auburn_weather_monitor/  application, validation, and reporting logic
tests/                       offline tests and API fixtures
data/raw/                    committed raw API response
data/processed/              committed processed forecast CSV
docs/data-dictionary.md      output schema and provenance
reports/                     authoritative Quarto source and rendered PDF
AGENTS.md                    durable contributor guidance
LICENSE                      MIT License
```

## Common Failures

- **API request failed:** Check internet access and try again. The National
  Weather Service may also be temporarily unavailable.
- **Validation failed:** The API response did not contain a required field or
  value type. Keep the error message and inspect the raw service behavior before
  changing the model.
- **User-agent not configured:** Copy `.env.example` to `.env` and replace the
  placeholder email.
- **`uv` or `quarto` not found:** Install the missing tool and open a new
  terminal before rerunning the documented command.
- **Dashboard does not open:** Use the exact Streamlit command above and open
  the local URL printed in the terminal.

## License and Maintainer Guidance

This project is available under the [MIT License](LICENSE). Contributors should
read [AGENTS.md](AGENTS.md) before changing project behavior or documentation.

## Known Limitations

- Forecasts depend on the availability and current schema of the National
  Weather Service API.
- The dashboard runs locally and is not deployed.
- The project reports forecast periods for one coordinate pair at a time. It
  does not compare locations or verify forecast accuracy.
