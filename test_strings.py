
def test_upper():
    assert a.upper() == "PYTEST"
def test_lower():
    assert a.islower() == False
def test_capitalize(a):
    assert a.capitalize() == "Pytest"
def test_failure():
    assert a.islower() == True

a = "pYtest"
test_capitalize(a)




