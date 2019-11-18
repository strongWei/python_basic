#!/bin/python
# 9-6 exercise
# @author strong
# @email 1025155365@qq.com

from Restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print('flavors:')
        for flavor in self.flavors:
            print('\t' + flavor)

flavors = [ '1', '2', '3' ]
res = IceCreamStand("strong", "goods", flavors)
res.describe_restaurant()
res.open_restaurant()
res.display_flavors()


