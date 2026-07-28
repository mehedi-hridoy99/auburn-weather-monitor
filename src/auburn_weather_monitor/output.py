import csv
import json
from pathlib import Path


CSV_FIELDS = [
    "number",
    "name",
    "start_time",
    "end_time",
    "temperature",
    "temperature_unit",
    "wind_speed",
    "wind_direction",
    "short_forecast",
]


def save_raw_json(data: dict, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def save_processed_csv(records: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(records)
