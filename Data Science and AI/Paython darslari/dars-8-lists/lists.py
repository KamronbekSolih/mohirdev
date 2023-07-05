# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 03:44:24 2023

@author: Kamronbek Solih
"""
# 8 - dars. Ro'yxatlar bilan ishlash

# =============================================================================
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# 
# #cars.sort() #ro'yxatni aslini o'zgartirdi
# print(cars)
# 
# print(sorted(cars)) #asl ro'yxat o'zgarmadi
# print(cars)
# =============================================================================

# =============================================================================
# oraliq = range(1,10) range()
# print(oraliq)
# =============================================================================

# =============================================================================
# # Ro'yxatlarni kesish
# 
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# print(cars)
# print(cars[3:5])
# =============================================================================


# =============================================================================
# # O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
# 
# davlatlar = ['Albaniya','Belarus','Canada',"denmark",'Ethiopiya','Finland','Great Britan', 'Hungary','Italy','Japan']
# # =============================================================================
# # # denmark ataylab kichkina harf bilan yozildi saralashda e'tibor tortishi uchun
# # print(davlatlar)
# # #Ro'yxatning uzunligini konsolga chiqaring
# # print(len(davlatlar))
# # 
# # #sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
# # # sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
# # print(sorted(davlatlar,reverse=True))
# # 
# # #Asl ro'yxatni qaytadan konsolga chiqaring
# # print(davlatlar)
# # 
# # #reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
# # davlatlar.reverse()
# # print(davlatlar)
# # =============================================================================
# 
# #sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqa
# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)
# =============================================================================

# =============================================================================
# #120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
# sonlar = list(range(120,1200,2))
# print(sonlar)
# #Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
# print(sum(sonlar))
# #Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
# ayirma = max(sonlar) - min(sonlar)
# print(ayirma)
# #Ro'yxatdagi elementlar sonini hisoblang
# print(len(sonlar))
# #Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
# boshidan = sonlar[:20]
# urtasidan = sonlar[len(sonlar)//2:(len(sonlar)//2+20)]
# oxiridan = sonlar[519:540]
# print(boshidan," ",urtasidan," ", oxiridan)
# =============================================================================

#taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting

taomlar = ['qazonkabob','chuchvara','osh','norin','manti']
print(taomlar)

#nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]
#Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta.remove("qazonkabob")
nonushta.remove("norin")
nonushta.remove("chuchvara")
nonushta.append("qatiq")
nonushta.append("qaymoq")
print(nonushta)

#Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
#Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta = tuple(nonushta)
nonushta[0] = "qatiq va qaymoq" #TypeError: 'tuple' object does not support item assignment







































