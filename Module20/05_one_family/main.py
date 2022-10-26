phone_book = {
    ('Сидоров', 'Никита') : 35,
    ('Сидорова', 'Алина') : 34,
    ('Сидоров', 'Павел') : 10,
    ('Иванова', 'Мария') : 27,
    ('Иванов', 'Андрей') : 44,
    ('Петров', 'Иван') : 37,
    ('Петрова', 'Анна') : 33
}


surname = input('Введите фамилию: ').lower()
new_surname = ''
if surname[-1] == 'а':
    new_surname = surname[:-1]
else:
    new_surname = surname + 'а'


count = 0
for people, age in phone_book.items():
    if surname in people[0].lower() or new_surname in people[0].lower():
        print(people[0], people[1], age)
        count += 1

if count == 0:
    print('Такого контакта нет.')

