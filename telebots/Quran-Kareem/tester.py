import requests
from pprint import pprint

oyat = "https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/ara-quran-la4/2/255.json"
tafsir = "https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu/2/255.json"
qiroat = "http://api.alquran.cloud/v1/ayah/2:255/ar.alafasy"
surov = requests.get(tafsir)
pprint(surov.json())