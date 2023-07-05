# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 06:52:32 2023

@author: Kamronbek Solih
"""

# 6-dars. Matn


# =============================================================================
# kocha = 'Bog\'bon'
# mahalla = 'Sog\'bon'
# tuman = 'Bodomzor'
# viloyat = 'Samarqand'
# 
# manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"  #fsting -  matn ichida o'zgaruvchilardan foydalashning qulay usuli
# 
# print(manzil)
# =============================================================================

# =============================================================================
# # Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
# 
# kocha = input("Ko'cha: ")
# mahalla = input("Mahalla: ")
# tuman = input("Tuman: ")
# viloyat = input("Viloyat: ")
# 
# manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
# 
# print(manzil)
# 
# =============================================================================

# =============================================================================
# #Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
# 
# kocha = input("Ko'cha: ")
# mahalla = input("Mahalla: ")
# tuman = input("Tuman: ")
# viloyat = input("Viloyat: ")
# 
# manzil = f" {kocha} ko'chasi,\n {mahalla} mahallasi,\n {tuman} tumani,\n {viloyat} viloyati"
# 
# print(manzil)
# =============================================================================

#Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang
# manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.

kocha = 'bog\'bon'
mahalla = 'sog\'bon'
tuman = 'bodomzor'
viloyat = 'Samarqand'

adres = [kocha,mahalla,tuman,viloyat]
adres1=[]

for i in adres:
    adres1.append(i.capitalize())
    
manzil1 = f"{adres1[0], adres1[1], adres1[2], adres1[3]}"

manzil = f"{kocha}, {mahalla}, {tuman}, {viloyat}"

print(adres1)
