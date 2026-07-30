"""Define Pydantic contracts for required NWS response fields."""

from pydantic import BaseModel, ConfigDict, Field


class PointProperties(BaseModel):
    """Required properties from the NWS points response."""
    model_config = ConfigDict(extra="allow")

    forecast: str = Field(min_length=1)


class PointResponse(BaseModel):
    """Validated subset of the NWS points response."""
    model_config = ConfigDict(extra="allow")

    properties: PointProperties


class ForecastPeriod(BaseModel):
    """Required fields for one NWS forecast period."""
    model_config = ConfigDict(extra="allow")

    number: int
    name: str = Field(min_length=1)
    startTime: str = Field(min_length=1)
    endTime: str = Field(min_length=1)
    temperature: int | float
    temperatureUnit: str = Field(min_length=1)
    windSpeed: str
    windDirection: str
    shortForecast: str = Field(min_length=1)


class ForecastProperties(BaseModel):
    """Validated forecast-period collection."""
    model_config = ConfigDict(extra="allow")

    periods: list[ForecastPeriod]


class ForecastResponse(BaseModel):
    """Validated subset of the NWS gridpoint forecast response."""
    model_config = ConfigDict(extra="allow")

    properties: ForecastProperties
