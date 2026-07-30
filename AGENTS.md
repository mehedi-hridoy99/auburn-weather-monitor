# AGENTS.md

## Project Context

Auburn Weather Monitor is a small Python project that retrieves, validates, and
processes National Weather Service forecast data. The CLI and Streamlit
dashboard use the same service layer.

The project uses a `src/` layout, `uv`, Pydantic, Streamlit, pytest, and Quarto.

## Setup and Checks

Restore the environment and run the full test suite:

```bash
uv sync
uv run python -m pytest
```

Run the CLI help and dashboard smoke checks when changing user-facing behavior:

```bash
uv run auburn-weather-monitor --help
uv run streamlit run src/auburn_weather_monitor/dashboard.py
```

Rebuild the report from the repository root with:

```bash
quarto render reports/auburn-forecast-report.qmd
```

## Navigation and Conventions

- Keep external HTTP behavior in `src/auburn_weather_monitor/api.py`.
- Keep Pydantic response contracts in `models.py`.
- Keep CLI parsing and orchestration in `cli.py`.
- Keep browser-only presentation in `dashboard.py`.
- Keep shared request-to-record behavior in `service.py`.
- Keep reusable report loading and analysis in `reporting.py`.
- Keep output writing in `output.py`.
- Prefer focused functions with type hints and concise docstrings.
- Use fixture data and mocks for tests. Automated tests must not call the live API.
- Update the README and data dictionary when commands or output fields change.
- Do not commit `.env`, private contact information, logs, caches, or virtual environments.

## Sources of Truth

- `README.md`: user setup, commands, examples, and troubleshooting
- `docs/data-dictionary.md`: processed CSV fields and transformations
- `reports/auburn-forecast-report.qmd`: authoritative report source
- `pyproject.toml` and `uv.lock`: dependencies and reproducible environment
- `tests/`: expected behavior and failure handling
- `data/`: committed submission data used by the report

This file contains durable project guidance. Task lists and session notes do not
belong here.
