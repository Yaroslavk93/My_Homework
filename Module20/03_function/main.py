def slicer(new_tuple, element):
    if element in new_tuple:
        if new_tuple.count(element) > 1:
            frs_i = new_tuple.index(element)
            snd_i = new_tuple.index(element, frs_i + 1) + 1
            return new_tuple[frs_i : snd_i]
        else:
            return new_tuple[new_tuple.index(element):]
    else:
        return ()


from random import randint
random_tuple = (tuple([randint(1, 10) for i in range(10)]), randint(1, 10))
print(f'Начальный список: {random_tuple}')
print(f'Ответ в консоли: {slicer(random_tuple[0], random_tuple[1])}')



