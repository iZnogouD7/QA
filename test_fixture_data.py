#kei reuse garnu paryo bhani use
#like prepare resources

import pytest
@pytest.fixture
#scope=method,id,class,seesion
def sample_data():
    return {"a":1,"b":2}
def test_sample(sample_data):
    assert sample_data["a"] == 1
    assert sample_data["b"] == 2