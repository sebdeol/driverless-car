from typing import Generator

import pytest

from app.car import Car


@pytest.fixture
def car() -> Generator:
    yield Car()
