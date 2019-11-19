#!/bin/python
# 10-2 exercise
# @author strong
# @email 1025155365@qq.com

with open('learning_python.txt') as file_object:
    while True:
        line = file_object.readline()
        if line:
            cline = line.replace('python', 'java').replace('\n','')
            print(cline)

        else:
            break

