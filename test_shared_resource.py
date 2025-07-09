import pytest

#session ma both pass
#module ma both pass because of resource sharing
#function raw class ma second fail hunxa. each has its own instance

@pytest.fixture(scope="function")
def shared_resource():
    return {"count":0}

def test_one(shared_resource):
    shared_resource["count"] += 1
    assert shared_resource["count"] == 1

def test_two(shared_resource):
    shared_resource["count"] += 1
    assert shared_resource["count"] == 1
