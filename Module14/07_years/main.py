def function (year1, year2):
    for digit in range(year1, year2 + 1):
        a,b,c,d = digit // 1000, digit // 100 % 10, digit // 10 % 10, digit % 10
        if a == b == c or b == c == d or c == d == a or a == b == d:
            print(a * 1000 + b * 100 + c * 10 + d)


print('При вводе года используйте четырёхзначное число.')
while True:
    first_year = int(input('Введите первый год: '))
    last_year = int(input('Введите второй год: '))
    if first_year >= 10000 or first_year < 1000 or last_year >= 10000 or last_year < 1000:
        print('Вы ввели неверное значение. Введите четырёхзначные числа ещё раз\n')
    else:
        break

print('\nГода от', first_year, 'до', last_year, 'с тремя одинаковыми цифрами:')
function(first_year, last_year)