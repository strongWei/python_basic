#!/bin/python
# 6-1 exercise
# @author strong
# @email 1025155365@qq.com

userInfo = {
    'first_name': 'strong',
    'last_name': 'Wei',
    'age': 28,
    'city':'Jieyang'
}

for key,value in userInfo.items():
    print(key + ':' + str(value))
