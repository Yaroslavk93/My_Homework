from tick_tac_toe import Player, Game


print(
    'Перед вами таблица с номерами каждой клетки:\n'
    '1 | 2 | 3\n'
    '---------\n'
    '4 | 5 | 6\n'
    '---------\n'
    '7 | 8 | 9\n'
)

player_1 = Player('Игрок 1', 'X')
player_2 = Player('Игрок_2', 'O')

winner = Game(player_1, player_2)
winner.game()
winner.result_game()
