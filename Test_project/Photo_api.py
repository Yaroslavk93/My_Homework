import requests
import jmespath
import re

url = "https://hotels4.p.rapidapi.com/properties/get-hotel-photos"

querystring = {"id":"1178275040"}

headers = {
	"X-RapidAPI-Key": "84865619demsh3627d7e1edcea9ep1f8f1ajsn0986565187aa",
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

b = jmespath.search("hotelImages[*].baseUrl", response.json())
#print(b)

for i in b:
    i = re.sub(r"{size}", "z", i)
    print(i)
