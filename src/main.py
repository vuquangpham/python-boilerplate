from utils.config import load_config
from utils.logging import get_logger, setup_logging


def main() -> None:
  """Main function."""
  # Load configuration
  config = load_config()

  # Set up logging
  setup_logging(config.logging)

  logger = get_logger()
  logger.info('Starting python-project application')


if __name__ == '__main__':
  main()
