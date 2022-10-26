line_1 = input('Первая строка: ')
line_2 = input('Вторая строка: ')

flag = False
for step in range(1, len(line_2)):
  line_2 = line_2[- 1] + line_2[: - 1]
  if line_2 == line_1:
    flag = True
    print(f'\nПервая строка получается из второй со сдвигом {step}.')
  else:
    continue

if not flag:
  print('\nПервую строку нельзя получить из второй с помощью циклического сдвига.')
