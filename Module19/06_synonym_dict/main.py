pair_list = [input(f'{text + 1} пара: ').lower().split() for text in range(int(input('Введите количество пар слов: ')))]

dict1 = dict()
for i in pair_list:
    dict1[i[0]] = i[2]
    dict1[i[2]] = i[0]

while True:
    word = input('\nВведите слово: ').lower()
    if word in dict1:
        print(f'Синоним: {dict1[word]}')
        break
    else:
        print('Такого слова в словаре нет.')
