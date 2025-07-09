import tempfile
import sys
def write_message(filepath, message):
    with open(filepath, 'w') as f:
        f.write(message)

def read_message(filepath):
    with open(filepath, 'r') as f:
        return f.read()

def read_temporary_file():
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp_path=temp.name

    messege=read_message(temp_path)
    print(messege)
    #message(temp_path,"Hello")
    #assert read_message(temp_path) == "Hello"
    #os.remove(temp_path)
