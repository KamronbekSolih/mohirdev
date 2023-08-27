from googletrans import Translator

tarjima = Translator()
word = tarjima.translate("hello","uz").text
print(word)
