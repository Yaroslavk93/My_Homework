text = input('Введите текст: ').lower()

orign_dict = dict()
for symbol in text:
    if symbol in orign_dict:
        orign_dict[symbol] += 1
    else:
        orign_dict[symbol] = 1

print('Оригинальный словарь частот:')
for letter in sorted(orign_dict):
    print(f'{letter} : {orign_dict[letter]}')

inverted_dict = {
    value : [i for i in sorted(orign_dict.keys()) if orign_dict[i] == value] for key, value in orign_dict.items()
}


print('\nИнвертированный словарь частот:')
for num in inverted_dict:
    print(f'{num} : {inverted_dict[num]}')