#!/bin/python
# 6-10 exercise
# @author strong
# @email 1025155365@qq.com

favorite_num = {}
favorite_num['strong'] = range(1,4)
favorite_num['helen'] = range(4,7)
favorite_num['selen'] = range(7,10)
favorite_num['len'] = range(10,13)
favorite_num['ken'] = range(13,16)

for name,nums in favorite_num.items():
    print(name.title())
    for num in nums:
        print('\t' + str(num))
