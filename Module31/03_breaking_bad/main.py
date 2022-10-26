import requests
import json


deaths_info = requests.get('https://breakingbadapi.com/api/deaths')
deaths_data = json.loads(deaths_info.text)


episodes_info = requests.get('https://www.breakingbadapi.com/api/episodes')
episodes_data = json.loads(episodes_info.text)


my_dict = dict()
with open('Breaking_Bad.json', 'w') as file:
    count_d = 0
    for dicts in deaths_data:
        if dicts['number_of_deaths'] > count_d:
            count_death = dicts['number_of_deaths']
            # my_dict['death_id'] = dicts['death_id']
            my_dict['season'] = dicts['season']
            my_dict['episode'] = dicts['episode']
            my_dict['number_of_deaths'] = dicts['number_of_deaths']
            my_dict['death'] = dicts['death']

    for elem in episodes_data:
        if my_dict['season'] == int(elem['season']) and my_dict['episode'] == int(elem['episode']):
            my_dict['episode_id'] = elem['episode_id']

    json.dump(my_dict, file, indent=4)

with open('Breaking_Bad.json', 'r') as file:
    data = json.load(file)
    for key, value in data.items():
        print(f'{key}: {value}')
