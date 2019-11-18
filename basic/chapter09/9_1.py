#!/bin/python
# 9-1 exercise
# @author strong
# @email 1025155365@qq.com

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + ':' + self.cuisine_type)

    def open_restaurant(self):
        print("on sale!")

res = Restaurant("strong", "goods")
res.describe_restaurant()
res.open_restaurant()


res = Restaurant("strong1", "goods1")
res.describe_restaurant()
res.open_restaurant()

res = Restaurant("strong2", "goods2")
res.describe_restaurant()
res.open_restaurant()
