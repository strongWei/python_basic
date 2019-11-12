#!/bin/python
# 3-6 exercise
# @author strong
# @email 1025155365@qq.com

names = []
names.append('strong')
names.append('eric')
names.append('helen')

print('welcom to my hostel, ' + names[0].title())
print('welcom to my hostel, ' + names[1].title())
print('welcom to my hostel, ' + names[2].title())

print('I have a bigger hostel!')
names.insert(0,'tom')
names.insert(2, 'turing')
names.append('small')
print('welcom to my hostel, ' + names[0].title())
print('welcom to my hostel, ' + names[1].title())
print('welcom to my hostel, ' + names[2].title())
print('welcom to my hostel, ' + names[3].title())
print('welcom to my hostel, ' + names[4].title())
print('welcom to my hostel, ' + names[5].title())
