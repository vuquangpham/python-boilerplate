"""Path utilities for the project."""

from pathlib import Path


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
ENV_ROOT = PROJECT_ROOT / '.env.local'
SOURCE_ROOT = PROJECT_ROOT / 'src'
