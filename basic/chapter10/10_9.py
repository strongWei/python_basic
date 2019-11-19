#!/bin/python
# 10-8 exercise
# @author strong
# @email 1025155365@qq.com

try:
    with open('cats.txt') as cat_file, open('dogs1.txt') as dog_file:
        for cat in cat_file:
            print(cat.rstrip())

        for dog in dog_file:
            print(dog.rstrip())
        
except FileNotFoundError as error:
    pass
