text = input('Сообщение: ')
buffer = ''
rev_text = ''

for letter in text:
  if letter.isalpha():
    buffer += letter
  else:
    rev_text += buffer[::-1] + letter
    buffer = ''

print(rev_text)