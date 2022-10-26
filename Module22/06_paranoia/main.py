import os
doc = os.path.abspath(os.path.join('text.txt'))
cipher_file = open(doc, 'w')
cipher_file.write('Hello\nHello\nHello\nHello')
cipher_file.close()

new_file = open(doc, 'r')
res = new_file.read().lower().split()


import string
count = 1
my_list = []
for word in res:
    result = ''
    for letter in word:
        if letter in string.ascii_lowercase and \
                string.ascii_lowercase.find(letter) + 1 != len(string.ascii_lowercase):
            result += string.ascii_lowercase[string.ascii_lowercase.find(letter) + count]
        else:
            result += string.ascii_lowercase[0 + (count - 1)]
    my_list.append(result.capitalize())
    count += 1

new_file.close()


cipher_text = open(os.path.abspath(os.path.join('cipher_text.txt')), 'w')
cipher_text.write(f'{my_list[0]}\n{my_list[1]}\n{my_list[2]}\n{my_list[3]}')
cipher_text.close()