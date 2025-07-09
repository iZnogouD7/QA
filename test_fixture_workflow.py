import pytest


@pytest.fixture(autouse=True)
def file_handler():
    print("Opening a file before yield")
    file=open("sample.txt","w")
    yield
    print("Closing file after yield")
    file.close()
