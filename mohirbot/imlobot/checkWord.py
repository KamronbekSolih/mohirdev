from latcyruz import toLatin, toCyrillic
from uzwords import words
from difflib import get_close_matches
import re


# print(get_close_matches(toCyrillic('maktap'),words,n=5))


def has_latin(text):
    return bool(re.search('[a-zA-Z]', text))

def checkWords(word, words=words):
    word = word.lower()
    if has_latin(word):
        word = toCyrillic(word)

    matches = set(get_close_matches(word,words))
    available = False

    if word in matches:
        available = True
        matches = word
    elif 'ҳ' in word:
        word = word.replace('ҳ','х')
        matches.update(get_close_matches(word,words))
    elif 'х' in word:
        word = word.replace('х','ҳ')
        matches.update(get_close_matches(word,words))
    return {'available':available, 'matches':matches}

    
if __name__=='__main__':
    print(checkWords("hato"))
    print(checkWords("tarih"))
    print(checkWords("xato"))
    print(checkWords("olma"))
    print(checkWords("hat"))
    print(checkWords("hayt"))

    print(toLatin(checkWords("olma")['matches']))