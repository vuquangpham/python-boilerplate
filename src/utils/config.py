from pathlib import Path
import sys
from typing import Any

import yaml

root_path = Path.joinpath(Path.cwd(), 'src')
config_path = Path.joinpath(root_path, 'configs/settings.yaml')


def load_config(
    config_path: Path = config_path,
) -> dict[str, Any]:
    """Load configuration from YAML file.

    Args:
        config_path: Path to the configuration file

    Returns:
        Dictionary containing configuration settings

    Raises:
        SystemExit: If configuration file is not found or invalid
    """
    try:
        print(config_path, Path.cwd(), Path(__file__))
        with Path.open(config_path) as config_file:
            config = yaml.safe_load(config_file)
            return config if config is not None else {}

    except FileNotFoundError:
        print(f'Error: Configuration file not found at {config_path}')
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f'Error: Invalid configuration file at {config_path}: {e}')
        sys.exit(1)
