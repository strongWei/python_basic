#!/bin/python
# 7-8 exercise
# @author strong
# @email 1025155365@qq.com
sandwich_orders = ['pizza1','pizza2','pizza3','pastrami','pastrami','pastrami']

print('The pastrami is off sale')

finished_sandwiches = []

while sandwich_orders:
    pizza = sandwich_orders.pop()
    if pizza != 'pastrami':
        finished_sandwiches.append(pizza)
        print('I made your ' + pizza + ' sandwich')
print('Finished')
