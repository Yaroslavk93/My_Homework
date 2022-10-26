skates_amt = int(input('Кол-во коньков: '))
N = []
for pair in range(skates_amt):
  print('Размер', str(pair+1) + '-й пары: ', end = '')
  size = int(input())
  N.append(size)
N.sort()

people_amt = int(input('\nКол-во людей: '))
K = []
for num_people in range(people_amt):
  print('Размер ноги', str(num_people + 1) + '-го человека: ', end = '')
  foot = int(input())
  K.append(foot)

count_people = 0
for people in K:
  for skates in range(len(N)):
    if N[skates] >= people:
      N.remove(N[skates])
      count_people += 1
      break

print('\nНаибольшее кол-во людей, которые могут взять ролики: ',count_people)
