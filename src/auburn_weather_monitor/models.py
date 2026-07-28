from pydantic import BaseModel, ConfigDict, Field


class PointProperties(BaseModel):
    model_config = ConfigDict(extra="allow")

    forecast: str = Field(min_length=1)


class PointResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    properties: PointProperties


class ForecastPeriod(BaseModel):
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
    model_config = ConfigDict(extra="allow")

    periods: list[ForecastPeriod]


class ForecastResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    properties: ForecastProperties
