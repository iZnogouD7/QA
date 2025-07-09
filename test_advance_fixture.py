import pytest
@pytest.fixture
def resource():
    print("Setting up resource")
    #setup
    yield "resource_value"
    #above yield is setup and below is teardown
    #teardown
    print("tearing down resource")
def test_resource(resource):
    print(resource)
    assert resource == "resource_value"
def test_new(resource):
    assert True;
# if no resource inside argument then it doesnt run for that test