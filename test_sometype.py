def test_sample_user(sample_user):
    assert sample_user["name"] == "Samir"
    assert sample_user["role"] == "principal"