#!/bin/python
# 6-3 exercise
# @author strong
# @email 1025155365@qq.com

words = {
    "Java": "java",
    "Php": "php",
    "C#":"net",
    "Html":"html",
    "CSS":"css"
}

for key,value in words.items():
    print(key + ':\n\t' + value)
