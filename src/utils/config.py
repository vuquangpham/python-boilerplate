from pathlib import Path
import sys

import yaml

from schemas.common import Common


def find_project_root() -> Path:
    """Find project root by looking for pyproject.toml."""
    current = Path(__file__).parent
    while current != current.parent:
        if (current / 'pyproject.toml').exists():
            return current
        current = current.parent
    raise RuntimeError('Could not find project root (no pyproject.toml found)')


# Use project root for all path calculations
PROJECT_ROOT = find_project_root()
root_path = PROJECT_ROOT / 'src'
config_path = root_path / 'config' / 'settings.yaml'


def load_config(
    config_path: Path = config_path,
) -> Common:
    """Load configuration from YAML file.

    Args:
        config_path: Path to the configuration file

    Returns:
        Common configuration object

    Raises:
        SystemExit: If configuration file is not found or invalid
    """
    try:
        with config_path.open() as config_file:
            config = yaml.safe_load(config_file)
            return Common(**config)

    except FileNotFoundError:
        print(f'Error: Configuration file not found at {config_path}')
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f'Error: Invalid configuration file at {config_path}: {e}')
        sys.exit(1)
