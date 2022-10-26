guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
 print('\nСейчас на вечеринке', len(guests), 'человек:', guests)
 command = input('Гость пришёл или ушёл? ')

 if command == 'пришёл':
   name1 = input('Имя гостя: ')
   if len(guests) < 6:
     guests.append(name1)
     print('Привет,', name1,'!')
   else:
     print('Прости,', name1, ', но мест нет.')

 elif command == 'ушёл':
   name2 = input('Имя гостя: ')
   for i in range(len(guests)):
     if name2 == guests[i]:
       guests.remove(name2)
       print('Пока,', name2,'!')
       break
   else:
     print('Такого гостя нет.')


 elif command == 'Пора спать':
   print('Вечеринка закончилась, все легли спать.')
   break

 else:
   print('Вы ввели неверное значение! Введите "ушёл", "пришёл" или "Пора спать".')