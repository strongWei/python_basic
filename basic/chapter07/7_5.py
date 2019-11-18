#!/bin/python
# 7-5 exercise
# @author strong
# @email 1025155365@qq.com
promt = 'Please enter your age to caculate the price:\n'
promt += 'Enter quit to end\n'

while True:
    age = input(promt)
    if age == 'quit':
        print('End program...') 
        break
    elif age.isdigit() == False:
        print('Please input a number:')
    else:
       age = int(age)
       if age < 3:
           print('The price is $0')
       elif age >= 3 and age < 12:
           print('The price is $10')
       else:
           print('The price is $15')
        
        
