# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 11:09:40 2023

@author: Kamronbek Solih

https://www.codewars.com/kata/583952fbc23341c7180002fd
"""
"""
Coding Meetup #14 - Higher-Order Functions Series - Order the food

You will be given an array of objects representing data about developers who have signed up to attend the next coding meetup that you are organising.

Your task is to return an object which includes the count of food options selected by the developers on the meetup sign-up form..

For example, given the following input array:
    
    list1 = [
    { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C', 'meal': 'vegetarian' },
    { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript', 'meal': 'standard' },
    { 'firstName': 'Ramona', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby', 'meal': 'vegan' },
    { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C', 'meal': 'vegetarian' },
]
"""

#Solution 1
# =============================================================================
# list1 = [
#     { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C', 'meal': 'vegetarian' },
#     { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript', 'meal': 'standard' },
#     { 'firstName': 'Ramona', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby', 'meal': 'vegan' },
#     { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C', 'meal': 'vegetarian' },
# ]
# 
# def order_food(lst): 
#     vgt = []
#     std = []
#     vgn = []
#     
#     for dev in lst: # taking each dictionary seperately since list1 is a list of dics
#         if dev['meal'] == 'vegetarian':   # if a dictionary's value 'meal' equals to ...
#             vgt.append(dev['meal'])
#         elif dev['meal'] == 'standard':
#             std.append(dev['meal'])
#         else:
#             vgn.append(dev['meal'])
#             
#     return { 'vegetarian': len(vgt), 'standard': len(std), 'vegan': len(vgn)}
# 
# print(order_food(list1))
# =============================================================================

#Solution 2 (Submitted for codewars)

def order_food(lst): 
    meals = []
    menyu = {}
    
    for dev in lst:
        meals.append(dev['meal'])
    categories = set(meals) # making a set from the list to get unique categories
    
    for category in categories:
        menyu[category] = meals.count(category) #filling up the dictionary with key:value pair
        
    return menyu
