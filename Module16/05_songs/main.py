violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

songs_num = int(input('Сколько песен выбрать? '))
count_time = 0

for i in range(songs_num):
 print('Название', str(i + 1) + '-й песни: ', end = '')
 my_song = input()
 for j in violator_songs:
   if j[0] == my_song:
     count_time += j[1]
     break
 else:
   print('Такой песни нет.')

print('\n\nОбщее время звучания песен:', round(count_time, 2),'минут')
