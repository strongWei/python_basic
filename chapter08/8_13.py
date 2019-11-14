#!/bin/python
# 8-13 exercise
# @author strong
# @email 1025155365@qq.com
def build_profile(first, last, **user_info):
     """ 创建一个字典，其中包含我们知道的有关用户的一切 """
     profile = {}
     profile['first_name'] = first
     profile['last_name'] = last
     for key, value in user_info.items():
         profile[key] = value
         return profile
def print_profile(profile):
    for key, value in profile.items():
        print(key + ': ' + value)

user_profile = build_profile('albert', 'einstein',
        location='princeton',
        field='physics')

print_profile(user_profile)
