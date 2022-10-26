def file_test(my_file, string):
    test_file = open(my_file, 'w', encoding='utf-8')
    test_file.write(string)
    test_file.close()


import os
text = input('Введите строку: ')
save_doc = input('\nКуда хотите сохранить документ? Введите последовательность папок (через пробел):\n').split()
name_doc = input('\nВведите имя файла: ')
file_path = os.path.abspath(os.path.join(os.path.sep, *(i for i in save_doc), name_doc + '.txt'))
#Users skipt Desktop Python_Basic Module22 Module22 05_save

if os.path.exists(file_path):
    check = input('Вы действительно хотите перезаписать файл? ').capitalize()
    if check == 'Да':
        file_test(file_path, text)
        print('Файл успешно перезаписан!')

else:
    file_test(file_path, text)
    print('Файл успешно сохранён!')


test_file = open(file_path, 'r', encoding='utf-8')
print(f'\nСодержимое файла:\n{test_file.read()}')
test_file.close()