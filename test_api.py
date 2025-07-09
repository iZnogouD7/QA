import requests
from unittest.mock import patch
def get_status(url):
    response=requests.get(url)
    return response.status_code

@patch('requests.get')
def test_get_status(mock_get):
    mock_get.return_value.status_code=200
    #this is used for mocking data ie. the above code always send status 200
    assert get_status("http://example.com") == 200