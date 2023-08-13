import wikipedia

wikipedia.set_lang("uz")
sorov = "salom batafsil"

if "batafsil" in sorov:
    sorov = sorov.replace("batafsil","")
    print(wikipedia.page(sorov).content)
else:
    print(wikipedia.summary(sorov))