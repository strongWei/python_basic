#!/bin/python
# 10-11 exercise
# @author strong
# @email 1025155365@qq.com

import json

try:
    num = input('Please input one number: ')
    num = int(num)

    with open('number.txt','w') as file_object:
        json.dump(num, file_object)

    with open('number.txt') as file2_object:
        content = json.load(file2_object)
        print(content)

except ValueError as error:
    print('Please input a number!')
except FileNotFoundError as error2:
    print(error2.fileName + ' is not found!')
