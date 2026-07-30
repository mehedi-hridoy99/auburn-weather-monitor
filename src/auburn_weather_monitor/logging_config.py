"""Configure consistent console and optional file logging."""

import logging
from pathlib import Path


def configure_logging(level: str = "INFO", log_file: Path | None = None) -> None:
    """Configure root logging at ``level`` and optionally create ``log_file``."""
    handlers: list[logging.Handler] = [logging.StreamHandler()]
    if log_file is not None:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        handlers.append(logging.FileHandler(log_file, encoding="utf-8"))

    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        handlers=handlers,
        force=True,
    )
