# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 18:42:15 2023

@author: Kamronbek Solih
"""

# 17 dars. while TSIKLI

# =============================================================================
# '''
# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
# '''
# kitoblar = []
# 
# while True:
#     kitob = input("Yaxshi ko'rgan kitobingizni kiriting. \n (chiqish uchun exit deb yozing)")
#     if kitob == 'exit':
#         break
#     else:
#         kitoblar.append(kitob)
#         
# print(f"Siz yaxshi ko'rgan kitoblar ro'yxati {', '.join(kitoblar)}")
# =============================================================================


'''
Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm,
18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin.
Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).
Yuqoridagi dasturni turli usullarda yozib ko'ring (break, ishora, yoki shart tekshirish)
'''

# with break
# =============================================================================
# 
# while True:
#     yosh = input("Yoshingizni kiritng: ")
#     narx = 0
#     if yosh == 'exit' or yosh == 'quit':
#         break
#     elif int(yosh) <= 7:
#         narx = 2000
#         break
#     elif int(yosh) > 7 and int(yosh) <= 18:
#         narx = 3000
#         break
#     elif int(yosh) >18 and int(yosh)<= 65:
#         narx = 10000
#         break
#     
# print(f"Sizning yoshingiz {yosh}da sizga chipta narxi {narx} so'm")
# =============================================================================
        
# with flag
# =============================================================================
# 
# flag = True
# 
# 
# while flag:
#     
#     qiymat = input("Yoshingiz: ")   
#     
#     if qiymat == 'exit' or qiymat == 'quit':
#         flag = False
#         
#     yosh = int(qiymat)
#     narx = 0
#     
#     if yosh <= 7:
#         narx = 2000
#         
#     elif 7<yosh<=18:
#             narx = 3000          
#     elif 18<yosh<=65:
#             narx = 10000            
#     print(f"Sizning yoshingiz {yosh}da sizga chipta narxi {narx} so'm")   
#    
# =============================================================================
        
        
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    
    if qiymat=='exit':
        break
    
    if int(qiymat)<0:
        continue
    
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        