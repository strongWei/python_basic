#!/bin/python
# 7-8 exercise
# @author strong
# @email 1025155365@qq.com
sandwich_orders = ['pizza1','pizza2','pizza3']
finished_sandwiches = []

while sandwich_orders:
    pizza = sandwich_orders.pop()
    finished_sandwiches.append(pizza)
    print('I made your ' + pizza + 'sandwich')
print('Finished')
