#!/bin/python
# 8-7 exercise
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

print_album(make_album('strong','1'))
print_album(make_album('ken','12'))
print_album(make_album('ken','12', 12))
