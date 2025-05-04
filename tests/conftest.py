import pytest
from fastapi.testclient import TestClient

from aula08.app import app

@pytest.fixture
def client():
    return TestClient(app)