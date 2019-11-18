#!/bin/python
# 3-7 exercise
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

print('now, I only can invite two friend to my hostel')
print("sorry, I can't invite you to my hostel, " + names.pop())
print("sorry, I can't invite you to my hostel, " + names.pop())
print("sorry, I can't invite you to my hostel, " + names.pop())
print("sorry, I can't invite you to my hostel, " + names.pop())

print('welcom to my hostel, ' + names[0].title())
print('welcom to my hostel, ' + names[1].title())

del names[0]
del names[0]
print(names)
