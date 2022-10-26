from test_Life import House, Life

house = House(50, 0)
male = Life('Иван', house)
woman = Life('Анна', house)
people_list = [male, woman]
test = True

for day in range(365):
    print(f'\nДень {day + 1}:')
    for people in people_list:
        if people.bellyful < 0:
            print(f'{people.name} умер на {day + 1} день. Эксперимент не удался!')
            test = False
            break
        people.action()

    if not test:
        break

    if day == 364:
        print('Все выжили! ')
