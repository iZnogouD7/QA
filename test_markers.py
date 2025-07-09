import pytest
import sys
@pytest.mark.skip(reason="Feature has been disabled")
def test_feature():
    assert False;
@pytest.mark.slow
def test_heavy_calculation():
    assert sum(range(100000))>0;
@pytest.mark.fast
def test_simple_multiplication():
    assert 2*3==6;

@pytest.mark.skipif(sys.platform == "win32", reason="Doesn't support Windows")
def test_linux():
    assert True;

@pytest.mark.xfail(reason="Know Bug")
def test_failure():
    assert True;
