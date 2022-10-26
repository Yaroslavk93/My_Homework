import random

errors_list = [SystemError, TypeError, ValueError, Warning, PermissionError, InterruptedError, OSError]
summ_digit = 0

with open('out_file.txt', 'w') as digit_file:
    while True:
        num = int(input('Введите число: '))
        if 13 == random.randint(1, 13):
            raise random.choice(errors_list)('Вас постигла неудача!')
        else:
            summ_digit += num
            digit_file.write(f'{str(num)}\n')
            if summ_digit >= 777:
                print('Вы успешно выполнили условие для выхода из порочного цикла!')
                break
