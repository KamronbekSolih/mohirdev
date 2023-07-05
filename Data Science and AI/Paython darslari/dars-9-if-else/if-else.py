# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 05:57:47 2023

@author: Kamronbek Soliboev
"""
# dars 9. If-else statement

# =============================================================================
# #Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
# 
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# 
# for car in cars:
# # =============================================================================
# #     if car.lower()=="gm":
# #         print(car.capitalize())
# #     else:
# #         print(car.title())
# # =============================================================================
#         
#   #  print(car.upper()) if car.lower() == 'gm' else print(car.title())
#     
# #Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring
#     print(car.title()) if car.lower() != 'gm' else print(car.upper())
# =============================================================================

# =============================================================================
# #Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.
# 
# login = input("Login>>>")
# 
# if login.lower() == "admin":
#     print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {login.title()}!")
# =============================================================================

# =============================================================================
# #Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
# 
# print("Ikkita son kiriting")
# a = int(input("a: "))
# b = int(input("b: "))
# 
# if a==b: print("Sonlar teng") 
# =============================================================================

# =============================================================================
# #Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.
# 
# son = int(input("Istalgan son kiriting: "))
# 
# print(f"{son} musbat") if son>0 else print(f"{son} manfiy")
# =============================================================================


#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.
from math import sqrt
son = int(input("Son kiriting: "))
print(f"{son}ning ildizi {sqrt(son)}") if son>=0 else print("Musbat son kiriting")













































