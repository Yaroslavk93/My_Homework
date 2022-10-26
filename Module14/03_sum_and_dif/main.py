def summ_numbers (num1):
    summ = 0
    while num1 > 0:
        digit = num1 % 10
        summ += digit
        num1 //= 10
    print('Сумма цифр:', summ)
    return summ


def count_numbers (num2):
    count = 0
    while num2 > 0:
        count += 1
        num2 //= 10
    print('Кол-во цифр в числе:', count)
    return count


while True:
    N = int(input('Введите целое положительное число: '))
    if N <= 0:
        print('Вы ввели неверное значение. Введите больше 0.\n')
    else:
        break

summ_N = summ_numbers(N)
count_N = count_numbers(N)

print('Разность суммы и кол-ва цифр:', summ_N - count_N)