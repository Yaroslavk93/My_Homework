nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def list_function(digit_list):
    new_list = list()
    for index in digit_list:
        if isinstance(index, list):
            new_list.extend(list_function(index))
        else:
            new_list.append(index)

    return new_list


print('Ответ:', list_function(nice_list))
