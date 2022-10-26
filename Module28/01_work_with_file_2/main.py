import os


class File:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.name, self.mode)
        except IOError:
            self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type is FileNotFoundError:
            self.file.close()
            return True


file_path = os.path.abspath(os.path.join('.', input('Введите имя файла: ') + '.txt'))
with File(file_path, 'r') as result:
    result.write('Python')

