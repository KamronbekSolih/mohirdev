# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 11:04:01 2023

@author: Kamronbek Solih
"""
# =============================================================================
# '''
# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. 
#           Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring. 
#           Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. 
#           For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.
# 
# '''
# 
# olim = {
#         'ism':'Albert Enshteyn',
#         'yil':1879,
#         'joy':'Germaniya',
#         'asar':"The theory of relativity"}
# muhaddis = {
#     'ism':'Imom al-Buxoriy',
#     'yil':810,
#     'joy':"O'zbekiston",
#     'asar':"Sahih ul Buxoriy"}
# tadbirkor = {
#     'ism':'Ilon Mask',
#     'yil':1971,
#     'joy':"Janubiy Afrika",
#     'asar':'Liftoff'}
# 
# mashxurlar = [olim, muhaddis, tadbirkor]
# 
# for mashxur in mashxurlar:
#     print(f"{mashxur['ism']} {mashxur['yil']}-yilda {mashxur['joy']}. {mashxur['asar']} asari muallifi.")
# =============================================================================


# =============================================================================
# '''
# Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. 
#     Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang. 
#     Natijani konsolga chiqaring.
# '''
# sevimli_kinolar = {
#     'Doston':['Troya','Povorot ne tuda','Rux 5:13'],
#     'Dadam':["Prision Break","Kurtlar VVadiysi",],
#     "Man":['Pirats of Carribian','The queens gambit']}
# for inson in sevimli_kinolar:
#     print(f"{inson} {sevimli_kinolar[inson]} filmlarini yaxshi ko'rishadi'")
# =============================================================================

'''
Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang. 
Har bir davlat haqida ma'lumotni konsolga chiqaring.
'''

davlatlar = {
    'Singapore':    {
            'population':5454000,
            'gdp per capita':72794,
            'currency':"Singapore Dollar"},
    'Malasia':  {
        'population':33540000,
        'gdp per capita':11109,
        'currency':'Malaysian Ringgit'},
    'Japan':    {
        'population':125700000,
        'gdp per capita':39320,
        'currency':'Japanese Yen'}
    }

# =============================================================================
# for davlat in davlatlar:
#     print(f"{davlat} \n population:{davlatlar[davlat]['population']} \n gdp per capita: {davlatlar[davlat]['gdp per capita']} , \n currency: {davlatlar[davlat]['currency']}")
#     
# =============================================================================


'''
Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi so'ragan davlat haqida ma'lumot bering.
 Agar davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.
'''
davlat = input('davlat: ')
if davlat in davlatlar:
        print(f"{davlat} \n population:{davlatlar[davlat]['population']} \n gdp per capita: {davlatlar[davlat]['gdp per capita']} , \n currency: {davlatlar[davlat]['currency']}")
else:
    print("Bizda bu davlat haqida ma'lumot yo'q")


