#!/bin/python
# 8-12 exercise
# @author strong
# @email 1025155365@qq.com

def revIngrediants( *ingrediants ):
    print('Your ingrediants: ')
    for ingrediant in ingrediants:
        print('\t' + str(ingrediant))

revIngrediants(1,2,3)
revIngrediants(1,2)
revIngrediants(1)
