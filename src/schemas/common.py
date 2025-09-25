from pathlib import Path

from pydantic import Field
from pydantic.dataclasses import dataclass

from utils.paths import PROJECT_ROOT


@dataclass
class Logging:
    """Logging settings."""

    level: str = Field(default='INFO')
    format: str = Field(default='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    output: Path = Field(default=PROJECT_ROOT / 'logs')


@dataclass
class Common:
    """Common settings."""

    logging: Logging = Field(default=Logging())
