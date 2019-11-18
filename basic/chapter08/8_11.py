#!/bin/python
# 8-11 exercise
# @author strong
# @email 1025155365@qq.com

def show_magicians( magicians ):
    for magician in magicians:
        print(magician)

def make_great( magicians ):
    magLen = len( magicians )
    for key in range(0,magLen):
        magicians[key] = 'the Great ' + magicians[key]        

magicians = ['strong', 'ken', 'helen']
magiciansClone = magicians[:]
make_great( magiciansClone )
show_magicians(magicians)
show_magicians(magiciansClone)
