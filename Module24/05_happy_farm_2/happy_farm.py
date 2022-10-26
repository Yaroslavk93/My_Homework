class Potato:
    status = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
            self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print(f'Картошка на {self.index} грядке сейчас {Potato.status[self.state]}')


class PotatoPatch:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def all_is_ripe(self):
        if all([i_potato.is_ripe() for i_potato in self.potatoes]):
            return True

    def all_grow(self):
        print('Картошка растет!')
        for i_potato in self.potatoes:
            i_potato.grow()


class Gardener:

    def __init__(self, name, garden):
        self.name = name
        self.garden = garden
        self.picking = 0

    def garden_work(self):
        if self.garden.all_is_ripe():
            print('Вся картошка созрела! Можно собирать.\n')
            for i_potato in self.garden.potatoes:
                self.picking += 1
                i_potato.state = 0
            print(f'{self.name} собрал {self.picking} картофелин')

        else:
            print('\nКартошка ещё не созрела.')
            action = int(input(f'Отправить {self.name} ухаживать за картошкой? 1 - Да / 2 - Нет   '))
            if action == 1:
                self.garden.all_grow()
                self.garden.all_is_ripe()