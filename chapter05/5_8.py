#!/bin/python
# 5-8 exercise
# @author strong
# @email 1025155365@qq.com

users = ('admin','test1','test2','test3','test4')
login_user = 'test1'

if login_user in users:
    if login_user == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print('Hello ' + login_user +  ', thank you for logging in again')


