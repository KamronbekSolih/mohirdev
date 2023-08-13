import wikipedia
def sorov(til,matn): #recieves language and message from the sender
    wikipedia.set_lang(til)
    if "batafsil" in matn: # if sender asks further information
        matn1 = matn.replace("batafsil","").strip() # removes "batafsil"(means "more") from the message string
        return wikipedia.page(matn1).content #and returns whole page content
    else:
        return wikipedia.summary(matn)