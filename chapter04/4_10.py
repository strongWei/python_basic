#!/bin/python
# 4-10 exercise
# @author strong
# @email 1025155365@qq.com

list = [ num ** 3 for num in range(1,11) ]
for value in list:
    print(value)

print('The first three items in the list are:' + str(list[:3]))
print('Three items from the middle of the list are:' + 
        str(list[4:7]))
print('The last three items in the list are:' + str(list[-3:]))
