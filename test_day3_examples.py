import pytest
import sys

@pytest.mark.parametrize("a,result",[(2,0),(3,1),(4,0),(5,1)])
@pytest.mark.slow
def test_even_func(a,result):
    assert a%2 == result;

@pytest.mark.skipif(sys.platform == "win32",reason="Doesn't work on Windows")
def test_windows_skip():
    assert False;