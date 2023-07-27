# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 21:36:19 2023

@author: user
"""


file = open("number_pi.txt",'r').read()

def split_string_by_2_characters(input_string):
    return [input_string[i:i+2] for i in range(0, len(input_string), 2)]

sliced = split_string_by_2_characters(file)

def split_string_by_2_characters(input_string):
    return [input_string[i:i+2] for i in range(0, len(input_string), 2)]

sliced = split_string_by_2_characters(file)

file = open("pi_to_char.txt",'a+')
with open('pi_to_char.txt','a+') as file:
    for character in sliced:
        file.write(chr(int(character)))