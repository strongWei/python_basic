#!/bin/python
# 8-6 exercise
# @author strong
# @email 1025155365@qq.com

def city_county(city, country):
    return country.title() + ', ' + city.title()

print(city_county('Shenzhen', 'China'))
print(city_county('chongqing', 'China'))
print(city_county('beijing', 'China'))
