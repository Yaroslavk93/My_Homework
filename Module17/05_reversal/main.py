line = list(input('Введите строку: '))
count = 0
for symbol in line[::-1]:
 count -= 1
 if symbol == 'h':
   break

expand = [h for h in line[count - 1: line.index('h'): -1]]
print('Развёрнутая последовательность между первым и последним h: ', end = '')
for i in expand:
   print(i, end = '')