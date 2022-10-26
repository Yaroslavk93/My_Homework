import os
zen_file = os.path.abspath(os.path.join('..', '02_zen_of_python', 'zen.txt'))
new_file = open(zen_file, 'r')

string = [i[:-1] for i in new_file]
print(f'Количество строк: {str(len(string))}\n')


word = [line.split() for line in string]
count_word = sum([len(i_wd) for i_wd in word ])
print(f'Количество слов: {str(count_word)}\n')


letter = [x.lower() for i in word for j in i for x in j if x.lower().islower()]
print(f'Количество букв: {str(len(letter))}\n')


alphabet = 'abcdefghijklmnopqrstuvwxyz'
min_letter = [
    i for i in alphabet if letter.count(i) ==
              min([letter.count(j) for j in alphabet if letter.count(j) != 0])
]
print(f'Наиболее редкая буква: {min_letter[0]}')

new_file.close()


# result = open('new_text.txt', 'w', encoding='utf-8')
# result.write(f'Количество строк: {str(len(string))}\n')
# result.write(f'Количество слов: {str(count_word)}\n')
# result.write(f'Количество букв: {str(len(letter))}\n')
# result.write(f'Редкая буква: {min_letter[0]}')
# result.close()