#!/bin/python
# 6-11 exercise
# @author strong
# @email 1025155365@qq.com

cities = {}
cities['city1'] = {
    'country':'china',
    'population':12334444,
    'fact': 'good'
}
cities['city2'] = {
    'country':'usa',
    'population':14444,
    'fact': 'fuck'
}
cities['city3'] = {
    'country':'france',
    'population':144,
    'fact': 'nice'
}
    
for city,infos in cities.items():
    print(city)
    for key,value in infos.items():
        print('\t' + key + ':' + str(value))
