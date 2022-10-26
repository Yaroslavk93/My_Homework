def refactoring(first_l: list, second_l: list) -> str:
    for x in first_l:
        for y in second_l:
            result = x * y
            if result == 56:
                yield (
                    f'Произведение чисел {x} и '
                    f'{y} равны {result}'
                )


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

find_num = refactoring(list_1, list_2)
print(find_num)
for i in find_num:
    print(i)
