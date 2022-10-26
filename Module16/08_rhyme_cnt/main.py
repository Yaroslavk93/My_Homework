people_amt = int(input('Кол-во человек: '))
people_list = list(range(1, people_amt + 1))
out_num = int(input('Какое число в считалке? '))
print('Какое число в считалке?', str(out_num) + '-й человек')

start = 0
while len(people_list) > 1:
    print('\nТекущий круг людей:', people_list)
    print('Начало счёта с номера', people_list[start])
    start = (start + out_num - 1) % len(people_list)
    print('Выбывает человек под номером', people_list[start])
    people_list.remove(people_list[start])
    start %= len(people_list)

print('\nОстался человек под номером', people_list[0])
