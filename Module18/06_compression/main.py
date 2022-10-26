text = list(input('Введите строку: '))
count = 1 
cipher = []
for symbol in range(len(text)):
  if text[symbol] == text[(symbol + 1) % len(text)]:
    count += 1
  else:
    cipher.append(text[symbol] + str(count))
    count = 1

count2 = 1
if text[-1] == text[0]:
  for last_sym in range(-1, - len(text), - 1):
    if text[last_sym] == text[last_sym - 1]:
      count2 += 1
    else:
      cipher.append(text[last_sym] + str(count2))
      break

print('Закодированная строка:', ''.join(cipher))