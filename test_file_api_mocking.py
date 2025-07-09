import tempfile
import requests
#import sys
from unittest.mock import patch

def write_message(filepath, message):
    with open(filepath, 'w') as f:
        f.write(message)

def read_message(filepath):
    with open(filepath, 'r') as f:
        return f.read()

def test_read_temporary_file():
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp_path=temp.name

    write_message(temp_path, "Hello")
    messege=read_message(temp_path)
    assert "Hello" in messege

def get_status(url):
    response=requests.get(url)
    return response.status_code
@patch('requests.get')
def test_get_status(mock_get):
    mock_get.return_value.status_code=200
    #this is used for mocking data ie. the above code always send status 200
    assert get_status("http://example.com") == 200


