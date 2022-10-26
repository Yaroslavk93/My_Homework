letters = [text for text in input('Введите текст: ') if text in ('аиеёоуыэюя')]
print('Список гласных букв:', letters, '\nДлина списка:', len(letters))
