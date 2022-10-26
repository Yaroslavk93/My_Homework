symbol_list = 'abcd'
digit_tuple = (10, 20, 30, 40)
my_result = [(symbol_list[i], digit_tuple[i]) for i in range(len(digit_tuple))]

print('Результат:')
for result in my_result:
    print(result)