import random


class Card:

    def __init__(self, card, card_suit, point):
        self.card = card
        self.card_suit = card_suit
        self.point = point


class Deck:

    def __init__(self, suit, pack):
        self.card_deck = [Card(key, colour, value) for colour in suit for key, value in pack.items()]

    def distribution(self):
        my_card = random.choice(self.card_deck)
        self.card_deck.remove(my_card)
        return f'{my_card.card} {my_card.card_suit}', my_card.point


class Player:

    def __init__(self, name, full_deck):
        self.name = name
        self.full_deck = full_deck
        self.card_list = []
        self.record = 0

    def game(self):
        hand = self.full_deck.distribution()
        # print(f'{self.name}:\nКарты на руках: {self.hand}')
        self.card_list.append(hand)

    def player_cards_info(self):
        print(f'\nКарты {self.name}а:')
        for player_hand in self.card_list:
            print(player_hand[0], end='  ')
            if isinstance(player_hand[1], tuple):
                my_choice = int(input('Выберите 1 или 11: '))
                if my_choice == 1:
                    self.record += 1
                else:
                    self.record += 11
            else:
                self.record += player_hand[1]
        print(f'Набрано очков: {self.record}')

    def computer_cards_info(self):
        print(f'\n{self.name} открывает свои карты...')
        for computer_hand in self.card_list:
            print(computer_hand[0], end='  ')
            if isinstance(computer_hand[1], tuple):
                if self.record + 11 <= 21:
                    self.record += 11
                else:
                    self.record += 1
            else:
                self.record += computer_hand[1]
        print(f'Набрано очков: {self.record}')


class Result:

    def __init__(self, dealer, gamer):
        self.dealer = dealer
        self.gamer = gamer

    def win(self):
        while True:
            print('Дилер раздаёт по 2 карты...')
            for check in range(2):
                self.gamer.game()
                self.dealer.game()

            while True:
                self.gamer.player_cards_info()
                gamer_check = int(input('Взять ещё одну карту? 1 - да / 2 - нет\n'))
                if gamer_check == 1:
                    self.gamer.record = 0
                    self.gamer.game()
                else:
                    break

            while True:
                if self.dealer.record < 16:
                    dealer_check = random.randint(1, 2)
                    if dealer_check == 1:
                        self.dealer.record = 0
                        self.dealer.game()
                    else:
                        self.dealer.computer_cards_info()
                        break
                else:
                    self.dealer.computer_cards_info()
                    break

            if ((self.gamer.record > self.dealer.record) and self.gamer.record < 22)\
                    or (self.gamer.record < 22 and self.dealer.record > 21):
                print(f'\nПобеду одержал {self.gamer.name}')
                break
            elif ((self.gamer.record < self.dealer.record) and self.dealer.record < 22)\
                    or (self.dealer.record < 22 and self.gamer.record > 21):
                print(f'\nПобеду одержал {self.dealer.name}')
                break
            else:
                print('\nНичья!')
                break
