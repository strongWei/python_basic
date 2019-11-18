#!/bin/python
# 8-5 exercise
# @author strong
# @email 1025155365@qq.com

def describe_city(city, country = 'China'):
    print(city.title() + ' is in ' + country)

describe_city('Shenzhen')
describe_city('Shanghai')
describe_city('Los', "USA")
