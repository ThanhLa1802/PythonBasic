#Context Manager
from contextlib import contextmanager

class WriteFile():
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file
    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()

@contextmanager
def write_file(file_name, mode):
    f = open(file_name, mode)
    yield f
    f.close()

