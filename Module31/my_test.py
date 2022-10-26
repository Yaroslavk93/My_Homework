import requests
import json

my_rec = requests.get('https://swapi.dev/api/people/3/')
# print(my_rec.text)

data = json.loads(my_rec.text)
data['name'] = 'R10-D10'
print(data['name'])


with open('my_test.json', 'w') as file:
    json.dump(data, file, indent=4)

with open('my_test.json', 'r') as file:
    data = json.load(file)

print(data)