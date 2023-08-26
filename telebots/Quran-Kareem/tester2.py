import requests
oyat = "https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/ben-muhiuddinkhan-la/2/255.json"
url = "https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu/2/255.json"
surov = requests.get(oyat)
print(surov.json())