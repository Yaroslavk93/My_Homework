def check_string(account):
    if len(account) != 3:
        raise IndexError('НЕ присутствуют все три поля: IndexError.')
    elif not account[0].isalpha():
        raise NameError('Поле имени содержит НЕ только буквы: NameError.')
    elif '@' not in account[1] and '.' not in account[1]:
        raise SyntaxError('Поле «Имейл» НЕ содержит @ и .(точку): SyntaxError.')
    elif account[2].isdigit() and int(account[2]) < 10 or int(account[2]) > 99:
        raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99: ValueError.')


with open('registrations.txt', 'r', encoding='utf-8') as test_file:
    string_list = [string.split() for string in test_file]

good_data = open('registrations_good.txt', 'w', encoding='utf-8')
bad_data = open('registrations_bad.txt', 'w', encoding='utf-8')

for user in string_list:
    user_account = ' '.join(user)
    try:
        check_string(user)
        good_data.write(f'{user_account}\n')
    except(IndexError, NameError, SyntaxError, ValueError) as error:
        bad_data.write(f'{user_account}                            {error}\n')

good_data.close()
bad_data.close()
