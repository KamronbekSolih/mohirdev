# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 05:24:37 2023

@author: Kamronbek Solih
"""
# 14 - dars. Lug'atlar

# =============================================================================
# ''' otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting
#  (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring: 
#   Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
#                                                                                                                          '''
# otam = {
#         'ism': "Komiljon",
#         'yil':1973,
#         'joy':'Namangan, Nanay',
#         }
# singlim = {
#     'ism':"Marjona",
#     'yil':2004,
#     'joy':'Namangan, Chortoq'}
# 
# inim = {
#         'ism':'Doston',
#         'yil':2003,
#         'joy':'Namangan, Nanay'}
# 
# akam = {
#         'ism':'umidbek',
#         'yil':1987,
#         'joy':'namangan, nanay'}
# 
# oilam = [otam, singlim, inim, akam]
# 
# for inson in oilam:
#     print(f" ismi {inson['ism']}, {inson['yil']}-yilda, {inson['joy'].title()}da tug'ilgan")
# =============================================================================

# =============================================================================
# #Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin.
# # Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
# 
# taomlar = {
#     'otam':'dimlama',
#     'singlim':'manti',
#     'akam':'honim',
#     'ukam':'kalbaska',
#     'bonuxon':'pirog',
#     'man':'moshkichra'}
# for inson in taomlar.keys():
#    print(f"{inson} ning sevimli taomi {taomlar[inson]}")
# =============================================================================
        

''' Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, float, string, if, else va hokazo
 va har birining qisqacha tarjimasini yozing. 
 Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa,
 "Bunda so'z mavjud emas" degan xabarni chiqaring.
Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring

'''

py_lugat = {
    'float':'suzuvchi nuqtali raqamlar',
    'int': 'butun sonlar',
    'str':'matn',
    'dictionary':"lug'at",
    "list":"ro'yxat",
    "if":"agar",
    "else":"bo'lmasa",
    "console":"natija chiqadigan oyna",
    "key-value pair":"kalit-qiymat juftligi",
    "tuple":"o'zgarmas ro'yxat"
    }

# =============================================================================
# word = py_lugat.get(input("Termin kiritng: ").lower(),"Bunday so'z mavjud emas!")
# print(word)
# =============================================================================

word = input("Termin kiritng: ")
if py_lugat[word]:
    print(f"{py_lugat[word]}")
else:
    print("Bunday so'z mavjus emas!")
    
''''
Mohirdev's solution

kalit = input("Kalit so'z kiriting:").lower()
tarjima = python_izohli_lugati.get(kalit)
if tarjima==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
'''

































