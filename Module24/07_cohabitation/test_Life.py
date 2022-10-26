import random


class House:
    def __init__(self, food, money):
        self.food = food
        self.money = money


class Life:

    def __init__(self, name, home):
        self.name = name
        self.home = home
        self.bellyful = 50

    def satiety(self):
        self.bellyful += 1
        self.home.food -= 1
        return f'{self.name} ест. Сытость: {self.bellyful}, Еда в доме: {self.home.food}'

    def work(self):
        self.home.money += 1
        self.bellyful -= 1
        return f'{self.name} работает. Сытость: {self.bellyful}, Деньги в доме: {self.home.money}'

    def shop(self):
        self.home.food += 1
        self.home.money -= 1
        return f'{self.name} идёт в магазин. Еда в доме: {self.home.food}, Деньги в доме: {self.home.money}'

    def play(self):
        self.bellyful -= 1
        return f'{self.name} играет. Сытость: {self.bellyful}'

    def action(self):
        num = random.choice(range(1, 7))

        if self.bellyful < 20:
            print(self.satiety())
        elif self.home.food < 10:
            print(self.shop())
        elif self.home.money < 50:
            print(self.work())
        elif num == 1:
            print(self.work())
        elif num == 2:
            print(self.satiety())
        else:
            print(self.play())
