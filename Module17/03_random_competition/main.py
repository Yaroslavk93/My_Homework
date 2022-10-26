import random

frt_list = [round(random.uniform(5, 10), 2) for _ in range(20)]
scd_list = [round(random.uniform(5, 10), 2) for _ in range(20)]
thd_list_condition = [(frt_list[i_point] if frt_list[i_point] > scd_list[i_point]
                       else scd_list[i_point]) for i_point in range(20)]

print('Первая команда:', frt_list)
print('Вторая команда:', scd_list)
print('Победители тура:', thd_list_condition)