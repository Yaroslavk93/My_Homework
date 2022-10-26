import requests
import jmespath


url = "https://hotels4.p.rapidapi.com/locations/v2/search"

querystring = {"query":"new york","locale":"en_US","currency":"USD"}

headers = {
	"X-RapidAPI-Key": "84865619demsh3627d7e1edcea9ep1f8f1ajsn0986565187aa",
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)


a = jmespath.search("suggestions[2].entities[*].name", response.json())
print(a)