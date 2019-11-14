#!/bin/python
# 8-8 exercise
# @author strong
# @email 1025155365@qq.com

def make_album(user_name, album_name, song_num = ''):
    album = {}
    album['user_name'] = user_name
    album['album_name'] = album_name
    if song_num :
        album['song_num'] = song_num
    return album

def print_album(album):
    for key, value in album.items():
        print(key + ":" + str(value))

while True:
    user_name = input('Please input user name: ')
    if user_name == 'quit':
        break
    album_name = input('Please input album name: ')
    if album_name == 'quit':
        break
    song_num = input('Please input song num: ')
    if song_num == 'quit':
        break
    print_album(make_album(user_name, album_name, song_num))

