#!/bin/python
# 10-4 exercise
# @author strong
# @email 1025155365@qq.com

promt = 'Please input you name \n'
promt += 'Enter q to quit: '
users = []
while True:
    userName = input(promt)
    if userName == 'q':
        break
    else:
        users.append(userName)

with open('guest.txt', 'a') as file_object:
    for user in users:
        file_object.write(user + '\n')
