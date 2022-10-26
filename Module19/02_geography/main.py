country_num = int(input('Количество стран: '))

country_dict = dict()
for num in range(country_num):
    country = input('{} страна: '.format(num + 1)).split()
    for city in range(len(country[1:])):
        country_dict[country[0]] = [town for town in country[1:]]
    for city in country[1:]:
        country_dict[city] = country[0]


for i in range(3):
    city_name = input('\n{} город: '.format(i + 1))
    if country_dict.get(city_name):
        print('Город {} расположен в стране {}.'.format(city_name, country_dict.get(city_name)))
    else:
        print('По городу {} данных нет.'.format(city_name))
