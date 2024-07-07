"""
Pytest configuration file.

This file is used to define global fixtures that can be used in all unit tests.
"""

import pytest
from dotenv import load_dotenv


@pytest.fixture(scope="session", autouse=True)
def _load_env_vars() -> None:
    """Load environment variables from .env file."""
    load_dotenv()
