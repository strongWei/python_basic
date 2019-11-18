#!/bin/python
# 9-3 exercise
# @author strong
# @email 1025155365@qq.com

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = 18

    def describe_user(self):
        print(self.first_name.title() + ' ' + self.last_name.title())

    def greet_user(self):
        print('Hello, ' + self.first_name.title() + ' ' + self.last_name.title())

res = User("strong", "goods")
res.describe_user()
res.greet_user()


res = User("strong1", "goods1")
res.describe_user()
res.greet_user()

res = User("strong2", "goods2")
res.describe_user()
res.greet_user()
