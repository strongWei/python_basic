#!/bin/python
# 10-7 exercise
# @author strong
# @email 1025155365@qq.com

while True:
    num1 = input('Please input the first number: ')
    num2 = input('Please input the second number: ')
    
    try:
        num1 = int(num1)
        num2 = int(num2)
        print(str(num1) + '+' + str(num2) + '=' + str(num1 + num2))
        break
    except ValueError as error:
        print('Sorry, you should input the number!') 
