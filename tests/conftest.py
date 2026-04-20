import copy
import pytest
from fastapi.testclient import TestClient
import src.app as app_module
from src.app import app

ORIGINAL_ACTIVITIES = copy.deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities():
    # Restore original seed data before every test to prevent state leakage
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(ORIGINAL_ACTIVITIES))
    yield


@pytest.fixture
def client():
    return TestClient(app)
