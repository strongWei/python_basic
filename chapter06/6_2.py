#!/bin/python
# 6-2 exercise
# @author strong
# @email 1025155365@qq.com

favorite_num = {}
favorite_num['strong'] = 17
favorite_num['helen'] = 18
favorite_num['selen'] = 19
favorite_num['len'] = 20
favorite_num['ken'] = 21

for name,num in favorite_num.items():
    print(name.title() + ':' + str(num))
