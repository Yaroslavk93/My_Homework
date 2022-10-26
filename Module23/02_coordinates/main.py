import random


def function_1(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    if y == 0:
        raise ZeroDivisionError('Ошибка в 1 функции.\nНа 0 делить нельзя!')
    else:
        return x / y


def function_2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    if x == 0:
        raise ZeroDivisionError('Ошибка во 2 функции.\nНа 0 делить нельзя!')
    else:
        return y / x


with open('coordinates.txt', 'w') as digit_file:
    x_num, y_num = random.randint(0, 10), random.randint(0, 5)
    digit_file.write(f'{x_num}\n{y_num}')

try:
    res1 = function_1(x_num, y_num)
    res2 = function_2(x_num, y_num)
    random_num = random.randint(0, 100)
    my_list = sorted([res1, res2, random_num])
    with open('result.txt', 'w') as result_file:
        result_file.write('\n'.join(map(str, my_list)))

except ZeroDivisionError as err:
    print(err)
