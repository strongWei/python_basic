#!/bin/python
# 5-10 exercise
# @author strong
# @email 1025155365@qq.com

current_users = ('admin','test1','test2','test3','test4')
new_users = ('admin','test','Test2','test31','test41')

usedLen = len(current_users)
idx = 0
for nUser in new_users:
    idx = 0
    for usedUser in current_users:
        if nUser.lower() == usedUser.lower():
            print('You need to input other user')
            break
        else:
            idx = idx + 1
            if idx >= usedLen : 
                print(nUser + ' has not be used')
