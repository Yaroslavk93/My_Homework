import random


class fight:

    def __init__(self, name, HP=100):
        self.name = name
        self.HP = HP

    def defensive(self):
        self.HP -= 20
        print(f'{self.name} осталось {self.HP} HP\n')

    def attack(self):
        print(f'{self.name} атакует')


warriors = [fight('Воин-1'), fight('Воин-2')]

while True:
    i_warrior = random.randrange(len(warriors))
    warriors[i_warrior].attack()
    warriors[i_warrior - 1].defensive()
    if warriors[i_warrior - 1].HP <= 0:
        print(f'{warriors[i_warrior].name} одержал победу!')
        break
