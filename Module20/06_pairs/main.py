from random import randint
origin_list = [randint(1, 10) for i in range(10)]
frst, snd = [origin_list[i] for i in range(0, len(origin_list), 2)], [origin_list[i] for i in range(1, len(origin_list), 2)]
final_list = list(zip(frst, snd))

print(f'Оригинальный список: {origin_list}')
print(f'Новый список: {final_list}')
