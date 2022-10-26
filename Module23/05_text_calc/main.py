expressions = ('100 + 34', '10 +* 3', '20 -* 2', '23 / 4')
with open('calc.txt', 'w') as calc_file:
    for exp in expressions:
        calc_file.write(f'{exp}\n')


def test_function(elem_list, sym_num=0):
    if elem_list[1] == '+':
        sym_num += int(elem_list[0]).__add__(int(elem_list[2]))
        return sym_num
    elif elem_list[1] == '-':
        sym_num += int(elem_list[0]).__sub__(int(elem_list[2]))
        return sym_num
    elif elem_list[1] == '*':
        sym_num += int(elem_list[0]).__mul__(int(elem_list[2]))
        return sym_num
    elif elem_list[1] == '/':
        sym_num += int(elem_list[0]).__truediv__(int(elem_list[2]))
        return sym_num
    elif elem_list[1] == '//':
        sym_num += int(elem_list[0]).__floordiv__(int(elem_list[2]))
        return sym_num
    elif elem_list[1] == '%':
        sym_num += int(elem_list[0]).__mod__(int(elem_list[2]))
        return sym_num
    else:
        calc_string = ' '.join(elem_list)
        raise TypeError(f'Обнаружена ошибка в строке: {calc_string} Хотите исправить? ')


sym_calc = 0
for i_elem in expressions:
    symbol_list = i_elem.split()
    try:
        result = test_function(symbol_list)
        sym_calc += result
    except TypeError as error:
        correct_err = input(error).lower()
        if correct_err == 'да':
            correct_text = input('Введите исправленную строку: ').split()
            correct_result = test_function(correct_text)
            sym_calc += correct_result
        else:
            pass

print(sym_calc)