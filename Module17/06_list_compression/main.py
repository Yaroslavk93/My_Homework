import random

before = [random.randint(0, 2) for _ in range(int(input('Количество чисел в списке: ')))]
after = list([N for N in before if N > 0] + [0] * before.count(0))
after = after[:after.index(0)]

print('Список до сжатия:', before)
print('Список после сжатия:', after)