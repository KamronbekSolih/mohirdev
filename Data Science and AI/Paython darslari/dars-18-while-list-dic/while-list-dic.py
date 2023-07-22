# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 21:44:26 2023

@author: Kamronbek Solih
"""

# =============================================================================
# """
# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
# """
# mahsulotlar = []
# 
# while True:
#     
#     mahsulot = input("Qaysi mahsulotni xarid qilmoqchisiz? (chiqish uchun 'chiqish' deb yozing) \n")
#     
#     if mahsulot != 'chiqish':
#         mahsulotlar.append(mahsulot)
#     else:
#         break
#     
# for mahsulot in mahsulotlar:
#     print(f"{mahsulot},")
# =============================================================================

# =============================================================================
# 
# """
# e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. Foydalanuvchidan lug'atga 
# bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
# 
# """
# 
# mahsulotlar = {}
# 
# while True:
#     mahsulot = input("Mahsulot: ")
#     narx = int(input("Narx: "))
#     mahsulotlar[mahsulot] = narx
#     takror = input("Yana mahsulot qo'shasizmi? ha/yo'q")
#     if takror != 'ha':
#         break
#     else:
#         continue
#     
# for mahsulot, narx in mahsulotlar.items():
#     print(f"{mahsulot}ning narxi {narx} so'm")
# =============================================================================



# Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring 
# (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa 
#  mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.

buyurtmalar = []
while True:
    buyurtma = input("Buyurtmangiz: ")
    print("Chiqish uchun 'tugat' deb yozing")
    if buyurtma == 'tugat':
        break
    else:
        buyurtmalar.append(buyurtma)
        print("Yana biror nima qo'shamizmi?")

ombor = {
    'banan':2500,
    'sabzi':1000,
    'sut':5000,
    'yogurt':5000,
    'olma': 5000
}
narx = 0
for buyurtma in buyurtmalar:
    if buyurtma in ombor:
        print(f"{buyurtma} ning narxni {ombor[buyurtma]}")
        narx += ombor[buyurtma]
    else:
        print(f'{buyurtma} do\'konimizda yo\'q')

print("Siz",end=' ')
for buyurtma in buyurtmalar:
    if buyurtma in ombor:
        print(buyurtma,end=', ')
print("tanladingiz. Jami buyurtmalaringiz narxi ",narx," von")
