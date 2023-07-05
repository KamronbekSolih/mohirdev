# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 03:59:49 2023

@author: Kamronbek Solih
"""
# dars 8. for loop

# =============================================================================
# #Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
# 
# ismlar = ["Muhammad Ali", "Shukrulloh"," Husan Yahyo Abdulmajid", "Jack London", "Anvar Narz"]
# n = 0
# for ism in ismlar:
#     print(f"Hurmatli {ism} ustoz, Men sizni ilmingizni xurmat qilaman va o'zimga ustoz sifatida ko'raman.")
#     n+=1
# #Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing
# print("Kod ",n," marta takrorlandi")
# 
# # Another way: print(f"Kod {len(ismlar)} marta takrorlandi")
# =============================================================================

# =============================================================================
# #10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
# 
# toq_sonlar = list(range(10,101,2))
# 
# for son in toq_sonlar:
#     print(f"{son} ning kubi {son**3}\n")
# =============================================================================

# =============================================================================
# #Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
# kinolar = []
# for i in range(5):
#     kinolar.append(input("Sevimli kinoingizni nomini kiriting: "))
#     
# print("Siz mana bu kinolarni yoqtirasiz ",kinolar)
# 
#  ''' mohirdev's way:
#      
#      print("5 ta sevimli kinoingiz qaysilar?")
# for k in range(5):
#     kinolar.append(input(f"{k+1}-kino:"))
# print(kinolar)  
# 
# '''
# =============================================================================

#Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring

suhbatdoshlar = []

sbdsh_soni = int(input("Bugun nechta odam bilan suhbatlashdingiz?"))
print("Ular kimlar?")

for suhbatdosh in range(sbdsh_soni):
    suhbatdoshlar.append(input(f'{suhbatdosh+1} chi suhbatdoshingizni ismi: '))
    
print("Siz bugun ",suhbatdoshlar," bilan shubatlashgansiz")











































