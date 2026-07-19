from pathlib import Path


DEFAULT_USER_AGENT = "auburn-weather-monitor/0.1 (contact email not configured)"


def load_env(path: Path = Path(".env")) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        return values

    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def get_user_agent() -> str:
    env = load_env()
    return env.get("NWS_USER_AGENT", DEFAULT_USER_AGENT)
