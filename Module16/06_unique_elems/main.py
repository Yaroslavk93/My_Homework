first_list = []
second_list = []

for list1 in range(3):
 print('Введите', str(list1 + 1) + '-е число для первого списка: ', end = '')
 num1 = int(input())
 first_list.append(num1)

print()

for list2 in range(7):
 print('Введите', str(list2 + 1) + '-е число для второго списка: ', end = '')
 num2 = int(input())
 second_list.append(num2)

print('\nПервый список:', first_list)
print('Второй список:', second_list)
first_list.extend(second_list)

for i in range(len(first_list)):
 while first_list.count(i) > 1:
   first_list.remove(i)

print('\nНовый первый список с уникальными элементами: ', first_list)