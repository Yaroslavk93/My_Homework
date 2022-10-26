#lesson7
import os
first_tour = open(os.path.abspath(os.path.join('firs_tour.txt')), 'w')
point = 80
start_list = {
    'Ivanov Serg': 80,
    'Segeev Petr': 92,
    'Petrov Vasiliy': 98,
    'Vasiliev Maxim': 78
}
first_tour.write(f'{point}\n')
for key, value in start_list.items():
    first_tour.write(f'{key} {str(value)}\n')

finish_tuple = {}
for key, value in start_list.items():
    new_list = []
    if value > 80:
        for name in reversed(key.split()):
            new_list.append(name)
        new_list[0] = new_list[0][:1] + '.'
        finish_tuple[' '.join(new_list)] = value


sorted_dict = {}
for num in reversed(sorted(finish_tuple.values())):
    for key in finish_tuple.keys():
        if finish_tuple[key] == num:
            sorted_dict[key] = finish_tuple[key]
            break

first_tour.close()


second_tour = open(os.path.abspath(os.path.join('second_tour.txt')), 'w')
second_tour.write(f'{str(len(sorted_dict))}\n')
count = 1
for name, record in sorted_dict.items():
    second_tour.write(f'{count}) {name} {str(record)}\n')
    count += 1
second_tour.close()