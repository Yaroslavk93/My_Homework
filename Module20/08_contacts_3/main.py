phone_book = dict()
while True:
    action = int(input(
        '\nВведите номер действия:\n   '\
        '1. Добавить человека\n   '\
        '2. Найти человека\n'
    ))

    if action == 1:
        contact = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').title().split())
        if contact not in phone_book:
            phone_book[contact] = int(input('Введите номер телефона: '))
            print(phone_book)
        else:
            print('Такой человек уже есть в контактах.')


    elif action == 2:
        surname = input('Введите фамилию для поиска: ').capitalize()

        if surname[-1] != 'a':
            new_surname = surname[:-1]

        count = 0
        for people, age in phone_book.items():
            if surname in people[1] or new_surname in people[1]:
                print(people[0], people[1], age)
                count += 1
        if count == 0:
            print('Данный человек отсутствует в телефонной книге.')

    else:
        print('Ошибка: Введите 1 или 2.')

    print('Текущий словарь контактов:', phone_book)