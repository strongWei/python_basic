#!/bin/python
# 10-3 exercise
# @author strong
# @email 1025155365@qq.com

promt = 'Please input you name: '
userName = input(promt)
with open('guest.txt', 'w') as file_object:
    file_object.write(userName) 
