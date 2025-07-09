import pytest


def div(a,b):
    return a/b
def test_subtraction():
    assert 10-5 == 5

def test_list():
    assert [1,2,3] == [1,2,3]

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        div(1,0)
