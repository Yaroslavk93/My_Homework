import math


class Circle:

    def __init__(self, X_num1, Y_num1, radius1):
        self.X_num1 = X_num1
        self.Y_num1 = Y_num1
        self.radius1 = radius1

    def volume(self):
        return round((math.pi * (self.radius1 ** 2)), 2)

    def perimeter(self):
        return round((2 * math.pi * self.radius1), 2)

    def intersection(self, X_num2, Y_num2, radius2):
        return math.sqrt(abs(self.X_num1 - X_num2) ** 2) + abs((self.Y_num1 - Y_num2) ** 2) <= self.radius1 + radius2


def print_func(size, S, P, r):
    if size == 0:
        print(f'Площадь = {S}')
        print(f'Периметр = {P}')
    else:
        print(f'Площадь = {S * size}')
        print(f'Периметр = {P * size}')
        r *= size
        return r


count_circle = 0
circle_list = []
while True:
    count_circle += 1
    data = Circle(int(input('\nВведите Х: ')), int(input('Введите Y: ')), int(input('Введите радиус: ')))
    increase = int(input('\nВо сколько раз увеличить круг? '))
    data.radius1 = print_func(increase, data.volume(), data.perimeter(), data.radius1)

    if len(circle_list) > 0:
        for i_elem in circle_list:
            if data.intersection(i_elem[1], i_elem[2], i_elem[3]):
                print(f'Круг {count_circle} пересекается с {i_elem[0]}')

    circle_list.append((f'Круг {count_circle}', data.X_num1, data.Y_num1, data.radius1))
