from math import sin, cos, radians


class Car:

    def __init__(self, name):
        self.name = name
        self.X = int(input('Введите координату Х: '))
        self.Y = int(input('Введите координату Y: '))
        self.direction = 0

    def move(self, distance):
        self.rotate(angle = int(input('Введите угол поворота: ')))
        direction_rad = radians(self.direction)

        if 0 < self.direction < 90:
            self.X += round(distance * cos(direction_rad), 2)
            self.Y += round(distance * sin(direction_rad), 2)
            print(
                f'\n{self.name} едет на Северо - Восток.\n'
                f'Новые координаты X = {self.X}, Y = {self.Y}'
            )

        elif 90 < self.direction < 180:
            self.X -= round(distance * cos(direction_rad), 2)
            self.Y += round(distance * sin(direction_rad), 2)
            print(
                f'\n{self.name} едет на Северо - Запад.\n'
                f'Новые координаты X = {self.X}, Y = {self.Y}'
            )

        elif 180 < self.direction < 270:
            self.X -= round(distance * cos(direction_rad), 2)
            self.Y -= round(distance * sin(direction_rad), 2)
            print(
                f'\n{self.name} едет на Юго - Запад.\n'
                f'Новые координаты X = {self.X}, Y = {self.Y}'
            )

        elif 270 < self.direction < 360:
            self.X += round(distance * cos(direction_rad), 2)
            self.Y -= round(distance * sin(direction_rad), 2)
            print(
                f'\n{self.name} едет на Юго - Восток.\n'
                f'Новые координаты X = {self.X}, Y = {self.Y}'
            )

        elif self.direction == 0 or self.direction == 360:
            self.X += distance
            print(
                f'\n{self.name} едет на Восток.\n'
                f'Новые координаты X = {self.X}, Y = {self.Y}'
            )

        elif self.direction == 90:
            self.Y += distance
            print(
                f'\n{self.name} едет на Север.\n'
                f'Новые координаты X = {self.X}, Y = {self.Y}'
            )

        elif self.direction == 180:
            self.X -= distance
            print(
                f'\n{self.name} едет на Запад.\n'
                f'Новые координаты X = {self.X}, Y = {self.Y}'
            )

        elif self.direction == 270:
            self.Y -= distance
            print(
                f'\n{self.name} едет на Юг.\n'
                f'Новые координаты X = {self.X}, Y = {self.Y}'
            )

    def rotate(self, angle):
        self.direction += angle
        self.direction %= 360

class Bus(Car):

    def __init__(self, name):
        super().__init__(name)
        self.passengers = 0
        self.money = 0
        self.amount_money = 0
        self.fare = int(input('Стоимость проезда, до следующей остановки: '))

    def entrance(self):
        self.passengers += int(input('Сколько пассажиров вошло? '))
        self.money = self.passengers * self.fare
        self.amount_money += self.money
        print(
            f'Пассажиров в автобусе: {self.passengers}\n'
            f'Получено денег: {self.money}'
        )

    def exit(self):
        self.passengers -= int(input(
            f'{self.name} доехал до остановки.\n'
            'Сколько пассажиров вышло? '
        ))

    def move(self, distance):
        self.entrance()
        super().move(distance)
        self.exit()


car = Car(name = 'Машина')
car.move(distance = int(input('Расстояние до следующего поворота: ')))
print()
bus = Bus(name = 'Автобус')
bus.move(distance = int(input('Расстояние до следующего поворота: ')))
# while True:
#     car.move()


#
#     def action(self):
#         num = int(input('\nСменить направление(1 - Да / 2 - Нет)? '))
#         if num == 1:
#             self.angle = int(input('Введите угол поворота: '))


    # def move(self):
        # self.new_coordinats()
        # direction = int(input('\nСменить направление(1 - Да / 2 - Нет)? '))
        # if direction == 1:
        #     self.angle = int(input('Введите угол поворота: '))
        #     self.distance = int(input('Расстояние для следующего поворота: '))



# a = 45
# d = 10 * cos(a)
# b = 270 % 360
# print(b)
# c = 10 * cos(b)
# print(c)
# print(d)
