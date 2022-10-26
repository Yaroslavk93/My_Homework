people_name = ['Василий', 'Николай', 'Надежда', 'Никита', 'Ян', 'Ольга', 'Евгения', 'Кристина']
with open('people.txt', 'w', encoding='utf-8') as people_file:
    for name in people_name:
        people_file.write(f'{name}\n')


string_count = 0
symbol_count = 0

with open('people.txt', 'r', encoding='utf-8') as open_file:
    text_read = open_file.read().split()

    for i_name in text_read:
        string_count += 1
        try:
            if len(i_name) < 3:
                raise TypeError(f'Ошибка: менее трёх символов в строке {string_count}.')
        except TypeError as err:
            print(err)
            import logging
            logging.basicConfig(filename='errors.log', encoding='utf-8')
            logging.error(err)

        symbol_count += len(i_name)
    print(f'Общее количество символов: {symbol_count}.')
