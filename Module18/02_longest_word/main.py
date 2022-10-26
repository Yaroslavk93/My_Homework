text = input('Введите строку: ').split()
letter_in_word = max([len(letter) for letter in text])
word_max = ([word for word in text if len(word) == letter_in_word])

print('Самое длинное слово:', ''.join(word_max))
print('Длина этого слова:', letter_in_word)