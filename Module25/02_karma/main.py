import random


class Errors:

    def __init__(self, error, karma):
        self.__error = error
        self.karma = karma

    def error_info(self):
        return f'\n{self.__error}\nВаша карма снизилась на {str(self.karma)}\n'


class KillError(Errors):
    def __init__(self, error, karma=7):
        super().__init__(error, karma)


class DrunkError(Errors):
    def __init__(self, error, karma=1):
        super().__init__(error, karma)


class CarCrashError(Errors):
    def __init__(self, error, karma=4):
        super().__init__(error, karma)


class GluttonyError(Errors):
    def __init__(self, error, karma=3):
        super().__init__(error, karma)


class DepressionError(Errors):
    def __init__(self, error, karma=2):
        super().__init__(error, karma)


class Life:
    def __init__(self, errors_list):
        self.errors_list = errors_list
        self.karma_count = 0

    def one_day(self):
        while True:
            self.karma_count += random.randrange(1, 7)
            accident_num = random.randrange(1, 10)
            if accident_num == 5:
                with open('karma.log', 'a', encoding='utf-8') as file:
                    accident = random.choice(self.errors_list)
                    accident.error_info()
                    file.write(accident.error_info())
                    self.karma_count -= accident.karma

            if self.karma_count >= 500:
                print('\nПоздравляю! Вы достигли просветления!')
                break


info = Life([
    DepressionError('Вы впали в депрессию.'),
    GluttonyError('Вы слишком много питаетесь.'),
    CarCrashError('Вы случайно поцарапали чью-то машину.'),
    DrunkError('Вы пьяны.'),
    KillError('Вы наступили на жука!')
])
info.one_day()
