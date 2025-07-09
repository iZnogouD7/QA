import pytest
@pytest.fixture(scope="module")
def db_connection():
    print("Connecting once for module")
    return "db_connection"
