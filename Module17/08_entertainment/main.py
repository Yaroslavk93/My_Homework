stick = list('|' * int(input('Количество палок: ')))

for shot in range(1, int(input('Количество бросков: ')) + 1):
    print('Бросок', str(shot) + '.', end = '')
    for target in range(int(input('Сбиты палки с номера ')) - 1, int(input('по номер '))):
        stick[target] = '.'

print('\nРезультат: ', end = '')
for i in stick:
    print(i, end = '')