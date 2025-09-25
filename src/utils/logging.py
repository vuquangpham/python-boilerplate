from datetime import datetime
import logging
import sys

from schemas.common import Logging


def setup_logging(config: Logging) -> None:
    """Set up logging configuration.

    Args:
        config: Configuration dictionary containing logging settings
    """
    level = getattr(logging, config.level)
    format_str = config.format

    # Create logs directory if it doesn't exist
    current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_path = config.output / f'cv_analyzer_{current_time}.log'
    log_path.parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=level,
        format=format_str,
        handlers=[logging.FileHandler(log_path), logging.StreamHandler(sys.stdout)],
    )


def get_logger(name: str = __name__) -> logging.Logger:
    """Get a logger with the given name."""
    return logging.getLogger(name)
