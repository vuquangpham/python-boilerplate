import os

from dotenv import load_dotenv
from pydantic import BaseModel, Field

from utils.paths import ENV_ROOT

load_dotenv(dotenv_path=ENV_ROOT)


class Env(BaseModel):
    """Environment variables."""

    EXAMPLE_KEY: str = Field(...)


env = Env(**os.environ)
