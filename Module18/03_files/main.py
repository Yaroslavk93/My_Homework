file = input('Название файла: ')
symbol = list('@№$%^&*()')

for i in symbol:
  if file.startswith(i):
    print('\nОшибка: название начинается на один из специальных символов.')

if not file.endswith(('.txt', '.docx')):
  print('\nОшибка: неверное расширение файла. Ожидалось .txt или .docx.')

else:
  print('\nФайл назван верно.')