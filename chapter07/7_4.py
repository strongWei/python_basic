#!/bin/python
# 7-4 exercise
# @author strong
# @email 1025155365@qq.com
promt = 'Please enter the ingredients of the pizza:\n'
promt += 'Enter quit to complete'

quit = False
ingredients = []
while quit == False:
    ingredient = input(promt)
    if ingredient == 'quit':
        print('The ingredients of your pizza:') 
        for value in ingredients:
            print('\t' + value)
        quit = True
    else:
        ingredients.append(ingredient)
