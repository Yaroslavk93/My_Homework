digit_list = [(1 if N % 2 == 0 else N % 5) for N in range(int(input('Введите длину списка: ')))]
print('Результат:',digit_list)