# import math
#
# def calculating_math_func(data):
#     result = (math.factorial(data) / data ** 3) ** 10
#     return result
#
# num = int(input('Введите число: '))
# print(calculating_math_func(num))

import math
def calculating_math_func(digit, data = dict()):
    if digit in data:
        return (data[digit] / digit ** 3) ** 10
    else:
        result = (math.factorial(digit) / digit ** 3) ** 10
        return result


num = int(input('Введите число: '))
print(calculating_math_func(num))
