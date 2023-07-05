# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 08:03:16 2023

@author: Kamronbek Solih
"""
# 15 - dars. Lug'atlar bilan ishlash

# =============================================================================
# ''' Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, 
# alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.
# '''
# 
# py_lugat = {
#     'float':'suzuvchi nuqtali raqamlar',
#     'int': 'butun sonlar',
#     'str':'matn',
#     'dictionary':"lug'at",
#     "list":"ro'yxat",
#     "if":"agar",
#     "else":"bo'lmasa",
#     "console":"natija chiqadigan oyna",
#     "key-value pair":"kalit-qiymat juftligi",
#     "tuple":"o'zgarmas ro'yxat"
#     }
# 
# for kalit, qiymat in sorted(py_lugat.items()):
#     print(f"{kalit} - {qiymat}")
# =============================================================================

# =============================================================================
# '''
# Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, 
# keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.
# '''
# dav_poy = {
#     "O'zbekiston":"Toshkent",
#     'Italiya':'Rim',
#     'Rossiya':'Moskva',
#     'Qozogiston':'Astana',
#     'Koreya Respublikasi':'Seul'}
# 
# for davlat in sorted(dav_poy.keys()):
#     print(davlat,'\n')
# 
# 
# for poytaxt in sorted(dav_poy.values()):
#     print(poytaxt)
# =============================================================================


# =============================================================================
# ''' Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring.
#  Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring. '''
#  
#  
# dav_poy = {
#       "O'zbekiston":"Toshkent",
#       'Italiya':'Rim',
#       'Rossiya':'Moskva',
#       'Qozogiston':'Astana',
#       'Koreya Respublikasi':'Seul'}
#  
# davlat = input("Qaysi davlatni poytaxtini bilmoqchisiz?")
# 
# if davlat in dav_poy:
#     print(f'{davlat} ning poytaxti {dav_poy[davlat]}')
# else:
#     print("Bizda bunday ma'lumot yo'q")
# =============================================================================
 
 
''' Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. 
Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring. '''
 
menyu = {
     'osh':10000,
     'Qozon kabob':11000,
     'qozon osh':12000,
     'tabaka':10000,
     'mastava':8000,
     'tiftel sho\'rva':7000,
     'achchiq go\'sht':11000,
     'chicken legs':10000,
     'chicken shashlik':5000,
     'somsa':4000}
 
print("3 ta ovqat buyurtma bering:")
 
buyurtmalar = []
 
for n in range(3):
     buyurtmalar.append(input(f'{n+1}chi buyurtmangiz: '))
     
 
for buyurtma in buyurtmalar:
    if buyurtma not in menyu:
        print("Bizda bunday taom yo'q")
    else:
        print(f"{buyurtma}ning narxi {menyu[buyurtma]} won")
 
 
 
 
 
 
 
 
 
 
 
 