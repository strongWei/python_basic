#!/bin/python
# 3-5 exercise
# @author strong
# @email 1025155365@qq.com

names = []
names.append('strong')
names.append('eric')
names.append('helen')

print('welcom to my hostel, ' + names[0].title())
print('welcom to my hostel, ' + names[1].title())
print('welcom to my hostel, ' + names[2].title())

print(names[1].title() + " can't come to my hostel")

names[1] = 'tom'
print('welcom to my hostel, ' + names[0].title())
print('welcom to my hostel, ' + names[1].title())
print('welcom to my hostel, ' + names[2].title())
