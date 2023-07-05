# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 08:58:39 2023

@author: Kamronbek Solih
"""

# dars 6. Sonlar

#Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur

import datetime

age = int(input("Yoshingizni kiriting: "))
time = datetime.datetime.now()
current_year = time.year
b_year = current_year - age

print("Siz", b_year,"chi yilda tug'ilgansiz.")