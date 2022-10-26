import random
user_name_list = input('Введите участников чата через пробел:\n').split()

while True:
    try:
        choice = int(input(
            '\nВыберите одно из действий:\n\
            1. Посмотреть текущий текст чата.\n\
            2. Отправить сообщение\n'
        ))

        if choice == 1:
            try:
                with open('chat.txt', 'r', encoding='utf-8') as chat_file:
                    for message in chat_file:
                        print(f'{message}')
            except FileNotFoundError:
                print('На данный момент сообщений нет. Попробуйте позже.')

        elif choice == 2:
            user = random.choice(user_name_list)
            user_message = input(f'Пользователь {user} вводит сообщение...\n')
            with open('chat.txt', 'a', encoding='utf-8') as message_file:
                message_file.write(f'{user}:   {user_message}\n')

        # elif choice == 777:
        #     raise ValueError('Вы ввели секретную команду и завершили чат для всех собеседников!')

        else:
            raise NameError('Ошибка: Такой команды не существует!')

    except NameError as error:
        print(error)
        # if ValueError:
        #     break

