import os
file_name = os.path.abspath(os.path.join('..', '..', 'Scratches'))
print(file_name)

name = os.listdir(file_name)
print(name)
subname = os.path.dirname(file_name)
print(subname)

size = 0
catalog = 0
count_files = 0
for path, dirs, files in os.walk(file_name):
    print('Path:     ', path)
    print('Dirs:     ', dirs)
    print('Files:    ',files)
    for index in files:
        count_files += 1
        size += os.path.getsize(os.path.join(path, index))
    catalog += len(dirs)


print(f'Размер каталога (в Кб): {size / 1024}')
print(f'Количество подкаталогов: {catalog}')
print(f'Количество файлов: {count_files}')