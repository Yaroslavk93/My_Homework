import random


class House:

    def __init__(self, food, money, pet_food, dirt):
        self.food = food
        self.money = money
        self.pet_food = pet_food
        self.dirt = dirt
        self.eaten_food = 0
        self.amount_salary = 0
        self.amount_coat = 0

class Family_life:

    def __init__(self, name, home):
        self.name = name
        self.home = home
        self.bellyful = 30
        self.mood = 100

    def eat(self):
        self.bellyful += 10
        self.home.food -= 10
        self.home.eaten_food += 10
        print(
            f'{self.name} ест. '
            f'Сытость: {self.bellyful}, '
            f'Количество еды в доме: {self.home.food}.'
        )

    def play(self):
        self.bellyful -= 10
        self.mood += 20
        print(
            f'{self.name} играет. '
            f'Сытость: {self.bellyful}, '
            f'Настроение: {self.mood}.'
        )

    def work(self):
        self.bellyful -= 10
        self.home.money += 150
        self.home.amount_salary += 150
        print(
            f'{self.name} работает. '
            f'Сытость: {self.bellyful}, '
            f'Денег в доме: {self.home.money}.'
        )

    def buy_food(self):
        self.home.money -= 20
        self.home.food += 20
        self.bellyful -= 10
        if self.home.pet_food < 50:
            self.home.money -= 10
            self.home.pet_food += 10
        print(
            f'{self.name} идёт в магазин. '
            f'Сытость: {self.bellyful}. '
            f'Количество еды в доме {self.home.food}, '
            f'Денег в доме {self.home.money}.'
        )

    def buy_coat(self):
        self.home.money -= 350
        self.mood += 60
        self.bellyful -= 10
        self.home.amount_coat += 1
        print(
            f'{self.name} покупает шубу. '
            f'Настроение: {self.mood}, '
            f'Сытость: {self.bellyful}, '
            f'Денег в доме: {self.home.money}.'
        )

    def tear_wallpaper(self):
        self.bellyful -= 10
        self.home.dirt += 5
        print(
            f'{self.name} дрёт обои. '
            f'Сытость: {self.bellyful}, '
            f'Порядок в доме: {self.home.dirt}.'
        )

    def sleep(self):
        self.bellyful -= 10
        print(
            f'{self.name} спит. '
            f'Сытость: {self.bellyful}.'
        )

    def cleaning(self):
        self.bellyful -= 10
        self.home.dirt = 0
        print(
            f'{self.name} наводит порядок. '
            f'Сытость: {self.bellyful}.'
        )

    def pet_the_cat(self):
        if self.mood == 100:
            pass
        else:
            self.mood += 5
            self.bellyful -= 10
        print(
            f'{self.name} гладит кота. '
            f'Настроение: {self.mood}'
        )

class Husband(Family_life):

    def __init__(self, name, home):
        super().__init__(name, home)

    def action(self):

        if self.bellyful <= 10:
            self.eat()
        elif self.mood <= 50:
            self.play()
        elif random.randrange(1, 5) == 3:
            self.pet_the_cat()
        else:
            self.work()

class Wife(Family_life):

    def __init__(self, name, home):
        super().__init__(name, home)

    def action(self):

        if self.home.food <= 70:
            self.buy_food()
        elif self.bellyful <= 10:
            self.eat()
        elif self.home.dirt >= 90:
            self.cleaning()
        elif self.mood <= 40 and self.home.money >= 500:
            self.buy_coat()
        elif self.home.money >= 2000:
            self.buy_coat()
        elif random.randrange(1, 5) == 3:
            self.pet_the_cat()
        else:
            self.buy_food()


class Cat(Family_life):
    def __init__(self, name, home):
        super().__init__(name, home)

    def eat(self):
        self.bellyful += 10
        self.home.pet_food -= 5
        print(
            f'{self.name} ест корм, '
            f'Сытость: {self.bellyful}. '
            f'Количество корма для животных: {self.home.pet_food}'
        )

    def action(self):
        if self.bellyful <= 10:
            self.eat()
        elif random.randrange(1, 2) == 2:
            self.tear_wallpaper()
        else:
            self.sleep()