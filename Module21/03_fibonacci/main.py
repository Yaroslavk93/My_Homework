def Fibonacci_series(position, digit_list, index):
    if index == position:
        return digit_list[index]
    else:
        number = digit_list[index - 1] + digit_list[index]
        digit_list.append(number)
        index += 1
        return Fibonacci_series(position, digit_list, index)

num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
Fibonacci_list = [0, 1]
num_index = 1

print('Число:', Fibonacci_series(num_pos, Fibonacci_list, num_index))