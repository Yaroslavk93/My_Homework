from Black_jack import Deck, Player, Result

while True:
    cards = Deck(
        ['Пики', 'Трефы', 'Червы', 'Бубны'],
        {
            'Двойка': 2, 'Тройка': 3, 'Четвёрка': 4,
            'Пятёрка': 5, 'Шестёрка': 6, 'Семёрка': 7,
            'Восьмёрка': 8, 'Девятка': 9, 'Десятка': 10,
            'Валет': 10, 'Дама': 10, 'Король': 10,
            'Туз': (1, 11)
        }
    )

    computer = Player('Дилер', cards)
    player = Player('Игрок', cards)

    winner = Result(computer, player)
    winner.win()

    repit_game = int(input('\nХотите сыграть ещё раз? 1 - ДА / 2 - НЕТ\n'))
    if repit_game == 1:
        continue
    else:
        break
