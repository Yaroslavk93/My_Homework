# TODO здесь писать код
friends = int(input('Кол-во друзей: '))
IOU = int(input('Долговых расписок: '))
#friends_list = list(range(1, friends + 1))
friends_list = []
for _ in range(friends):
  friends_list.append(0)

for num in range(IOU):
  print('\n' + str(num + 1) + '-я расписка')
  whom = int(input('Кому: '))
  whose = int(input('От кого: '))
  how_much = int(input('Сколько: '))
  friends_list[whom - 1] -= how_much
  friends_list[whose - 1] += how_much

print('\nБаланс друзей: ')
for i in range(len(friends_list)):
  print(str(i + 1) + ':',friends_list[i])