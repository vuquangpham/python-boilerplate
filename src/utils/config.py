from pathlib import Path
import sys

import yaml

from schemas.common import Common
from utils.paths import SOURCE_ROOT

config_path = SOURCE_ROOT / 'config' / 'settings.yaml'


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
