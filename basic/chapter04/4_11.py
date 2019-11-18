#!/bin/python
# 4-11 exercise
# @author strong
# @email 1025155365@qq.com

pizzas = ['pizza1','pizza2','pizza3']

friend_pizzas = pizzas[:]
pizzas.append('pizza4')

friend_pizzas.append('pizza5')

print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
