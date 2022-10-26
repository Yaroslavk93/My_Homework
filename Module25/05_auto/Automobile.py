from math import sin, cos, radians


class Car:

    def __init__(self, name):
        self.name = name
        self.X = int(input('Введите координату Х: '))
        self.Y = int(input('Введите координату Y: '))
        self.angle = int(input('Введите угол поворота: '))
        self.distance = int(input('Расстояние до следующего поворота: '))

    def move(self):
        while True:
            self.new_coordinates()
            direction = int(input(
                '\nСменить направление(1 - Да / 2 - Нет / 3 - Остановиться)? '
            ))
            if direction == 1:
                self.angle = int(input('Введите угол поворота: '))
                self.distance = int(input('Расстояние для следующего поворота: '))
            elif direction == 2:
                self.distance = int(input(
                    f'{self.name} едет прямо. '
                    f'Введите расстояние до следующего поворота: '
                ))
            else:
                print(f'{self.name} закончил движение.')
                break

    def new_coordinates(self):
        if 0 < self.angle < 90:
            self.X += round(cos(radians(self.angle)) * self.distance, 2)
            self.Y += round(sin(radians(self.angle)) * self.distance, 2)
            print(
                f'\n{self.name} едет на Северо - Восток.\n'
                f'Новые координаты X = {self.X}, Y = {self.Y}'
            )

        elif 90 < self.angle < 180:
            self.X -= round(cos(radians(180 - self.angle)) * self.distance, 2)
            self.Y += round(sin(radians(180 - self.angle)) * self.distance, 2)
            print(
                f'\n{self.name} едет на Северо - Запад.\n'
                f'Новые координаты X = {self.X}, Y = {self.Y}'
            )

        elif 180 < self.angle < 270:
            self.X -= round(cos(radians(270 - self.angle)) * self.distance, 2)
            self.Y -= round(sin(radians(270 - self.angle)) * self.distance, 2)
            print(
                f'\n{self.name} едет на Юго - Запад.\n'
                f'Новые координаты X = {self.X}, Y = {self.Y}'
            )

        elif 270 < self.angle < 360:
            self.X += round(cos(radians(360 - self.angle)) * self.distance, 2)
            self.Y -= round(sin(radians(360 - self.angle)) * self.distance, 2)
            print(
                f'\n{self.name} едет на Юго - Восток.\n'
                f'Новые координаты X = {self.X}, Y = {self.Y}'
            )

        elif self.angle == 0 or self.angle == 360:
            self.X += self.distance
            print(
                f'\n{self.name} едет на Восток.\n'
                f'Новые координаты X = {self.X}, Y = {self.Y}'
            )

        elif self.angle == 90:
            self.Y += self.distance
            print(
                f'\n{self.name} едет на Север.\n'
                f'Новые координаты X = {self.X}, Y = {self.Y}'
            )

        elif self.angle == 180:
            self.X -= self.distance
            print(
                f'\n{self.name} едет на Запад.\n'
                f'Новые координаты X = {self.X}, Y = {self.Y}'
            )

        elif self.angle == 270:
            self.Y -= self.distance
            print(
                f'\n{self.name} едет на Юг.\n'
                f'Новые координаты X = {self.X}, Y = {self.Y}'
            )


class Bus(Car):

    def __init__(self, name):
        super().__init__(name)
        self.passengers = 0
        self.money = 0
        self.amount_money = 0
        self.fare = int(input('\nСтоимость проезда, до следующей остановки: '))

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

    def move(self):
        while True:
            self.entrance()
            self.new_coordinates()
            self.exit()

            direction = int(input(
                '\nСменить направление(1 - Да / 2 - Нет / 3 - Остановиться)? '
            ))
            if direction == 1:
                self.angle = int(input('Введите угол поворота: '))
                self.distance = int(input('Расстояние для следующего поворота: '))
            elif direction == 2:
                self.distance = int(input(
                    f'{self.name} едет прямо. '
                    f'Введите расстояние до следующего поворота: '
                ))
            else:
                print(
                    f'{self.name} закончил движение.\n'
                    f'Заработано денег за всю поездку: {self.amount_money}'
                )
                break