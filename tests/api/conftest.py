from typing import Iterator

import pytest
from fastapi.testclient import TestClient

from ayomi.main import app


@pytest.fixture
def client() -> Iterator[TestClient]:
    yield TestClient(app)
