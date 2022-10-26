site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def structure(new_site, new_key, new_value):
    if new_key in new_site:
        new_site[new_key] = new_value
        return new_site

    for struct in new_site.values():
        if isinstance(struct, dict):
            result = structure(struct, new_key, new_value)
            if result:
                return new_site

import copy
site_dict = dict()
for _ in range(int(input('Сколько сайтов: '))):
    product = input('\nВведите название продукта для нового сайта: ')
    copy_site = copy.deepcopy(site)

    new_key = {'title': f'Куплю/продам {product} недорого', 'h2': f'У нас самая низкая цена на {product}'}
    active_site = {f'Сайт для {product}:': structure(copy_site, key, value) for key, value in new_key.items()}
    site_dict.update(active_site)

    print()
    for name, meaning in site_dict.items():
        print(f'{name}\n{meaning}')
