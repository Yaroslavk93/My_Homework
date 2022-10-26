string = set()
for symbol in input('Введите строку: '):
    if symbol in string:
        string.remove(symbol)
    else:
        string.add(symbol)

print(('Можно','Нельзя')[len(string) > 1], 'сделать палиндромом')
