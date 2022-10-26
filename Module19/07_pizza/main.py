order_list = [input(f'{num + 1} заказ: ').split() for num in range(int(input('Введите количество заказов: ')))]

order_dict = dict()
for i in order_list:
    if i[0] not in order_dict:
        order_dict[i[0]] = {i[1] : int(i[2])}
    else:
        if i[1] not in order_dict[i[0]]:
            order_dict[i[0]] |= {i[1] : int(i[2])}
        else:
            order_dict[i[0]][i[1]] += int(i[2])

for key, value in sorted(order_dict.items()):
    print(f'{key}:')
    for pizza, amount in sorted(value.items()):
        print(f'     {pizza}: {amount}')