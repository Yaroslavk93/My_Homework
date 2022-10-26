def tpl_sort(my_tuple):
    for digit in my_tuple:
        if not isinstance(digit, int):
            return my_tuple
    return tuple(sorted(my_tuple))


print(f'Ответ в консоли: {tpl_sort((6, 3, -1, 8, 4, 10, -5))}')
print(f'Ответ в консоли: {tpl_sort((3, -1.5, 8.9, -6, 11, 2))}')
