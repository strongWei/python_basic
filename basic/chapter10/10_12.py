#!/bin/python
# 10-12 exercise
# @author strong
# @email 1025155365@qq.com

import json

def get_stored_user(file_name):
    try:
        with open(file_name) as file_object:
            return json.load(file_object)
    except FileNotFoundError:
        return False
    
def store_user(file_name, user_name):
    with open(file_name, 'w') as file_object:
        json.dump(user_name, file_object)

num = input('Please input one color: ')

content = get_stored_user('color.txt')

if content == num:
    print('Your favorite color is ' + content)
else:
    store_user('color.txt', num)


