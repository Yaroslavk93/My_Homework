from Elements import Fire, Water, Air, Ground


def mix_elements(my_elem):
    mixing_elem = []
    if int(my_elem[0]) in range(1, 5) and int(my_elem[1]) in range(1, 5):
        if int(my_elem[0]) == 1 or int(my_elem[1]) == 1:
            mixing_elem.append(Fire())

        if int(my_elem[0]) == 2 or int(my_elem[1]) == 2:
            mixing_elem.append(Water())

        if int(my_elem[0]) == 3 or int(my_elem[1]) == 3:
            mixing_elem.append(Air())

        if int(my_elem[0]) == 4 or int(my_elem[1]) == 4:
            mixing_elem.append(Ground())
    else:
        raise IndexError('Вы ввели неверное значение! Выход из программы')

    frst_elem = mixing_elem[0]
    snd_elem = mixing_elem[1]
    return frst_elem, snd_elem


while True:
    elem_list = input(
        'Выберите элементы из списка через пробел:\n'
        '1 - Огонь; 2 - Вода; 3 - Воздух; 4 - Земля\n'
        '\nОтвет: '
    ).split()

    elem_1, elem_2 = mix_elements(elem_list)
    print(f'{elem_1.element} + {elem_2.element} = {elem_1 + elem_2}\n')
