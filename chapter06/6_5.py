#!/bin/python
# 6-5 exercise
# @author strong
# @email 1025155365@qq.com

words = {
    "River1": "Country1",
    "River2": "Country2",
    "River3": "Country3",
    "River4": "Country4",
    "River5": "Country5"
}

for key,value in words.items():
    print('the '+ key + ' run through ' + value)

for key in words:
    print(key)

for value in words.values():
    print(value)
