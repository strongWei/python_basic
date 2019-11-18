#!/bin/python
# 6-9 exercise
# @author strong
# @email 1025155365@qq.com

favorite_places = {
    "Tom": ['1','2','3'],
    "Sidy": ['4','5','6'],
    "Caty": ['7','8','9']
}

for uName, citys in favorite_places.items():
    print(uName)
    for city in citys:
        print('\t' + city)

