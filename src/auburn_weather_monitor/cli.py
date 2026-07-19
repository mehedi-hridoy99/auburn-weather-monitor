import argparse
from pathlib import Path

from auburn_weather_monitor.api import ApiError, fetch_forecast
from auburn_weather_monitor.config import get_user_agent
from auburn_weather_monitor.display import print_project_info, print_summary
from auburn_weather_monitor.output import save_processed_csv, save_raw_json
from auburn_weather_monitor.processing import forecast_periods


DEFAULT_LATITUDE = 32.6099
DEFAULT_LONGITUDE = -85.4808


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Fetch a National Weather Service forecast near Auburn, Alabama."
    )
    parser.add_argument("--latitude", type=float, default=DEFAULT_LATITUDE)
    parser.add_argument("--longitude", type=float, default=DEFAULT_LONGITUDE)
    parser.add_argument(
        "--raw-output",
        type=Path,
        default=Path("data/raw/forecast.json"),
    )
    parser.add_argument(
        "--processed-output",
        type=Path,
        default=Path("data/processed/forecast_periods.csv"),
    )
    parser.add_argument(
        "--project-info",
        action="store_true",
        help="Print setup information without calling the API.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    user_agent = get_user_agent()

    if args.project_info:
        print_project_info(user_agent)
        return

    try:
        raw_response = fetch_forecast(args.latitude, args.longitude, user_agent)
    except ApiError as error:
        raise SystemExit(str(error)) from error

    records = forecast_periods(raw_response)
    save_raw_json(raw_response, args.raw_output)
    save_processed_csv(records, args.processed_output)
    print_summary(records, args.raw_output, args.processed_output, raw_response["forecast_url"])


if __name__ == "__main__":
    main()
