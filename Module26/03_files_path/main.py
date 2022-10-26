import os


def gen_files_path(path, my_dir):
    for address, dirs, files in os.walk(path):
        for name in files:
            yield os.path.join(address, name)
        if my_dir in dirs:
            print('\nНайдена указанная директория: ')
            yield os.path.join(address, my_dir)
            return
    else:
        yield '\nДанной директории не существует'


file_path = os.path.abspath(os.path.sep)
dir_name = input('Введите имя директории: ')

for i_find in gen_files_path(file_path, dir_name):
    print(i_find)
