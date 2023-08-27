import requests
import json
app_id = "62b446b5"
app_key = "c2fe6960887f53b88999a767283d7e34"
language = "en-gb"
word_id = "example"
url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()


r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})

print(r.status_code)