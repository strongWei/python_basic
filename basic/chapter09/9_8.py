#!/bin/python
# 9-7 exercise
# @author strong
# @email 1025155365@qq.com
from User import User

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges
    def show_privileges(self):
        print('privileges:')
        for privilege in self.privileges:
            print('\t' + privilege)

class Admin(User):
    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)
        self.privileges = privileges

privileges = Privileges(['hello', 'world', 'here'])
res = Admin("strong", "goods", privileges)
res.privileges.show_privileges()
