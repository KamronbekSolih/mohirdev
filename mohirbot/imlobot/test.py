import re 

def has_cyrillic(text):
    return bool(re.search('[a-zA-Z]', text))

print(has_cyrillic("salom"))