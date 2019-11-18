#!/bin/python
# 6-6 exercise
# @author strong
# @email 1025155365@qq.com

favorite_languages = {
    "strong":"php",
    "helen":"java",
    "tom":"c#",
    "tony":"java"
}

search_user = ("strong","ken")

invitedUser = favorite_languages.keys()
for user in search_user:
    if user in invitedUser:
        print("Thank you," + user)
    else:
        print("Welcome to enter us," + user)
