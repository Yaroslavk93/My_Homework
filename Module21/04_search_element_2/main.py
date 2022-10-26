site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}


def find_key(site_dict, key, depth_length = -1):
    if depth_length == 0:
         return None
    if key in site_dict:
        return site_dict[key]

    for element in site_dict.values():
        if isinstance(element, dict):
            result = find_key(element, key, depth_length - 1)
            if result:
                break
    else:
        result = None

    return result


search_key = input('Введите искомый ключ: ')
depth = input('Хотите ввести максимальную глубину? Y/N: ').capitalize()

if depth == 'Y':
    max_depth = int(input('Введите максимальную глубину: '))
    print('Значение ключа:', find_key(site, search_key, depth_length=max_depth))
elif depth == 'N':
    print('Значение ключа:', find_key(site, search_key))
