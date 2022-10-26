from Life import *
house = House(food=50, money=100, pet_food=30, dirt=0)
man = Husband('Муж', house)
woman = Wife('Жена', house)
cat = Cat('Кот', house)
family_list = [man, woman, cat]
test = True

for day in range(365):
    print(f'\nДень {day + 1}:')
    for people in family_list:
        if people.bellyful < 0 or people.mood < 0:
            print(f'{people.name} умер на {day + 1} день. Эксперимент не удался!')
            test = False
            break
        people.action()

    if not test:
        break

    house.dirt += 5

    if day == 364:
        print(
            '\nВсе выжили!\n'
            'Заработано денег: {}\n'
            'Съедено еды за всё время: {}\n'
            'Куплено шуб: {}'.format(house.amount_salary, house.eaten_food, house.amount_coat)
        )

