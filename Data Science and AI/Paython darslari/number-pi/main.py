
file = open("number_pi.txt",'r').read()

def split_string_by_2_characters(input_string):
    return [input_string[i:i+2] for i in range(0, len(input_string), 2)]

sliced = split_string_by_2_characters(file)

i = 0
while i < len(sliced):
    sliced[i] = chr(int(sliced[i]))
    i += 1

    

print(sliced)

file = '123456789'

def split_string_by_2_characters(input_string):
    return [input_string[i:i+2] for i in range(0, len(input_string), 2)]

sliced = split_string_by_2_characters(file)

i = 0
while i < len(sliced):
    sliced[i] = chr(int(sliced[i]))
    i += 1

with open('pi2char.txt','a+') as file:
    for character in sliced:
        file.write(character)