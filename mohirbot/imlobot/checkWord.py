from uzwords import words
from difflib import get_close_matches

print(get_close_matches("маслаҳат",words, n = 5))
print(get_close_matches("Тинчлик",words))