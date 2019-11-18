#!/bin/python
# 9-4 exercise
# @author strong
# @email 1025155365@qq.com

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name + ':' + self.cuisine_type + ':' + str(self.number_served))

    def open_restaurant(self):
        print("on sale!")

    def set_number_served(self, number_served):
        self.number_served = number_served

res = Restaurant("strong", "goods")
res.describe_restaurant()
res.open_restaurant()

res.set_number_served(14)
res.describe_restaurant()
