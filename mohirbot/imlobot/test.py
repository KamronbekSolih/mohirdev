from uzwords import words
import checkWord

uzbeklatinwords = []
for word in words:
    word = checkWord.toLatin(word)
    uzbeklatinwords.append(f""{word}"")
to_string = "["+',\n'.join(uzbeklatinwords)+"]"

with open("uzwordslatin.py",'w') as file:
    file.write(to_string) 