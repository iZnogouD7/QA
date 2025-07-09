import pytest
@pytest.fixture(autouse=True)
def log_before_after():
    print("before test")
    yield
    print("after test")
def test_new_():
    print("This is test_new_")
    assert True

def test_very_new():
    print("This is test_very_new")
    assert True;