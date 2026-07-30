# Forecast Periods Data Dictionary

## Dataset

`data/processed/forecast_periods.csv` contains one row for each forecast period
returned by the National Weather Service gridpoint forecast endpoint.

Provenance:

- Provider: National Weather Service
- Points request: `https://api.weather.gov/points/32.6099,-85.4808`
- Location parameters: latitude 32.6099, longitude -85.4808
- Raw evidence: `data/raw/forecast.json`
- Processing code: `auburn_weather_monitor.processing.forecast_periods`

The application validates the forecast response with Pydantic and renames
selected API fields from camelCase to snake_case. It does not impute missing
values. An empty wind direction is allowed because calm periods can omit a
direction.

## Fields

| Field | Type | Units or values | Meaning and source | Missing-value rule / transformation |
|---|---|---|---|---|
| `number` | integer | Positive period sequence | NWS `number`; order within the forecast response | Required; copied without transformation |
| `name` | string | Examples: `Tonight`, `Friday` | NWS display name for the period | Required and non-empty |
| `start_time` | ISO 8601 string | Timestamp with UTC offset | NWS `startTime` | Required; renamed only |
| `end_time` | ISO 8601 string | Timestamp with UTC offset | NWS `endTime` | Required; renamed only |
| `temperature` | integer or float | Unit given by `temperature_unit` | NWS forecast temperature | Required; copied without conversion |
| `temperature_unit` | string | Usually `F` | NWS `temperatureUnit` | Required and non-empty |
| `wind_speed` | string | NWS text such as `5 mph` or `5 to 10 mph` | NWS `windSpeed` | Required string; range text is preserved |
| `wind_direction` | string | Compass direction such as `N`, `SW`, or empty | NWS `windDirection` | Required string; empty is allowed for calm wind |
| `short_forecast` | string | NWS weather description | NWS `shortForecast` | Required and non-empty |

## Important Limitations

The forecast is a service prediction, not an observation. Period lengths and
descriptions are determined by the National Weather Service. Temperature values
should only be compared after confirming that `temperature_unit` is consistent.
