#!/bin/python
# 8-14 exercise
# @author strong
# @email 1025155365@qq.com

def make_car(maker, no, **info):
    car = {
        'maker': maker,
        'no': no
    }
    for key, value in info.items():
        car[key] = value
    return car        

car = make_car('subaru', 'outback', color='blue',
        tow_package=True)
print(car)
