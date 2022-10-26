alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
message = input('Введите сообщение: ')
K = int(input('Введите сдвиг: '))

message2 = [(alphabet[(alphabet.index(sym) + K) % len(alphabet)] if sym != ' '
             else ' ') for sym in message]
cipher = ''
for i in message2:
  cipher += i

print('Зашифрованное сообщение:', cipher)
