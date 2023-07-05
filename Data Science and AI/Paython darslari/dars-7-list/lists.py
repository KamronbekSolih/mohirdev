# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 17:32:28 2023

@author: Kamronbek Solih
"""
# 7 dars. Ro'yxatlar


# =============================================================================
# 
# # ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
# 
# tekpe_sostav = ['Nozimjon',"Mo'minjon","Shohrux"]
# 
# # Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
# 
# print("Salom, ", tekpe_sostav[0]," bugun choyxona bormi?")
# print(tekpe_sostav[0]," bugun choyxonaga boramizmi? ")
# 
# print("Salom, ", tekpe_sostav[1]," bugun choyxona bormi?")
# print(tekpe_sostav[1]," bugun choyxonaga boramizmi? ")
# 
# print("Salom, ", tekpe_sostav[2]," bugun choyxona bormi?")
# print(tekpe_sostav[2],", bugun choyxonaga boramizmi? ")
# 
# # for tsiklini ishlashitshni bilmaganimdan emas hali u mavzuga yetib bormaganimizdan ishlatmadim
# =============================================================================


# =============================================================================
# #sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
# 
# sonlar = [12,2.4,32,17,-5,7.4]
# 
# print(sonlar[0]+sonlar[-2])
# print(sonlar[1]*sonlar[-1])
# print(sonlar[2]-sonlar[3])
# 
# print(sonlar)
# sonlar.append(16)
# print(sonlar)
# print(sonlar[2]//sonlar[-1])
# print(sonlar)
# del sonlar[4]
# print(sonlar)
# sonlar.remove(2.4)
# print(sonlar)
# sonlar.insert(2, 7)
# print(sonlar)
# =============================================================================

# =============================================================================
# 
# #t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
# 
# 
# # yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
#     
# t_shaxslar = ["Muhammad s.a.v","Z.M. Bobur","A. Navoiy", "Yusuf alayhissalom"]
# z_shaxslar = ["Mask", "Mirziyoyev", "Eshonqulov", "Shukrulloh domla"]
# 
# print("Men tarixiy shaxslardan", t_shaxslar.pop(0)," bilan, \nzamonaviy shaxslardan esa ", z_shaxslar.pop(0), "bilan shubat qilishni istar edim.")
#     
#     
#     
# =============================================================================
    
    
    
    
#friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.

friends = []
print(friends)
friends.append("Doston")
friends.append("Ismoil")
friends.append("Husniddin")
friends.append("Elbek")
friends.append("Oyatillo")
friends.append("Imomxo'ja")
    
print(friends)

#Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.

friends.remove("Husniddin")
del friends[1]

print(friends)

# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
    
friends.insert(0,"Mamajanov")
friends.insert(3,"Zohirbek")
friends.insert(-1,"Nodira")
friends.insert(5,"Mavzuna")

print(friends)
  # Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.  
mehmonlar = []

keldi = friends.pop(1)
mehmonlar.append(keldi)
    

keldi = friends.pop(5)
mehmonlar.append(keldi)

print(mehmonlar)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    