import pytest
@pytest.fixture
def fruit():
    return ["apple","cherry","banana"]

class TestFruits:
    def test_fruit(self,fruit):
        assert "apple" in fruit
    def test_length(self,fruit):
        assert len(fruit)==3
