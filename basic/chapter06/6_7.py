#!/bin/python
# 6-7 exercise
# @author strong
# @email 1025155365@qq.com

userInfo = {
    'first_name': 'strong',
    'last_name': 'Wei',
    'age': 28,
    'city':'Jieyang'
}

people = [
    userInfo,
    {
        'first_name': 'hello',
        'last_name': 'Wet',
        'age': 28,
        'city':'Jieyang'
    },
    {
        'first_name': 'ken',
        'last_name': 'Steven',
        'age': 28,
        'city':'Jieyang'
    }
]

for user in people:
    for key,value in user.items():
        print(key + ':' + str(value))
