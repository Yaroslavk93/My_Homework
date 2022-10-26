class Cell:
    cell_dict = {
        1: '', 2: '', 3: '',
        4: '', 5: '', 6: '',
        7: '', 8: '', 9: ''
    }

    @staticmethod
    def print_cell_board():
        print(f'\n{Cell.cell_dict[1]} | {Cell.cell_dict[2]} | {Cell.cell_dict[3]}')
        print('---------')
        print(f'{Cell.cell_dict[4]} | {Cell.cell_dict[5]} | {Cell.cell_dict[6]}')
        print('---------')
        print(f'{Cell.cell_dict[7]} | {Cell.cell_dict[8]} | {Cell.cell_dict[9]}')


class Player:

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.count = 0

    def tic_tac_toe(self):
        move = int(input(f'{self.name}, введите № клетки: '))
        if Cell.cell_dict[move] == '':
            Cell.cell_dict[move] = self.symbol
            self.count += 1
        else:
            print('Данная клетка уже занята!')

    def result(self):
        if Cell.cell_dict[1] == Cell.cell_dict[2] == Cell.cell_dict[3] \
                or Cell.cell_dict[4] == Cell.cell_dict[5] == Cell.cell_dict[6] \
                or Cell.cell_dict[7] == Cell.cell_dict[8] == Cell.cell_dict[9] \
                or Cell.cell_dict[1] == Cell.cell_dict[5] == Cell.cell_dict[9] \
                or Cell.cell_dict[3] == Cell.cell_dict[5] == Cell.cell_dict[9] \
                or Cell.cell_dict[1] == Cell.cell_dict[4] == Cell.cell_dict[7] \
                or Cell.cell_dict[2] == Cell.cell_dict[5] == Cell.cell_dict[8] \
                or Cell.cell_dict[3] == Cell.cell_dict[6] == Cell.cell_dict[9]:
            return True


class Game:

    def __init__(self, gamer_1, gamer_2):
        self.gamer_1 = gamer_1
        self.gamer_2 = gamer_2

    def game(self):
        while True:
            self.gamer_1.tic_tac_toe()
            if self.gamer_1.count + self.gamer_2.count == 9:
                Cell.print_cell_board()
                break
            self.gamer_2.tic_tac_toe()

    def result_game(self):
        if self.gamer_1.result():
            print(f'\nПобеду одержал {self.gamer_1.name}!')
        elif self.gamer_2.result():
            print(f'\nПобеду одержал {self.gamer_2.name}!')
        else:
            print('\nНичья.')
