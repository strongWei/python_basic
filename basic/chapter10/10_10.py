#!/bin/python
# 10-10 exercise
# @author strong
# @email 1025155365@qq.com

try:
    with open('book.txt') as file_object:
        content = file_object.read()
        count = content.count('us')
        print('The count of word is ' + str(count))
        
except FileNotFoundError as error:
   print(error.filename + ' is not found!')
