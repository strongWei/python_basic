#!/bin/pytho5
# 1-1 exercise
# @author strong
# @email 1025155365@qq.com
# data analyse: data clean

from csv import reader
from csv import writer

def handle_rows(line):
    """handle one line's content"""
    line[2] = strip_character(line[2], ['(',')'])
    if line[2] == '':
        line[2] = 'Nationality Unknown'
    else:
        line[2] = line[2].title()

    line[3] = date_to_int(line[3])
    line[4] = date_to_int(line[4])

    line[5] = strip_character(line[5], ['(',')'])
    if line[5] == '':
        line[5] = 'Gender Unknown'
    else:
        line[5] = line[5].title()

    line[6] = handle_date(line[6])

def handle_date(str):
    str = strip_character(str, ["(",")","c","C",".","s","'", " "])
    if not str:
        pass
    if '-' in str:
        str = str.split('-')
        str = round((int(str[0]) + int(str[1]) )/ 2)
    else:
        str = int(str)
    return str

def date_to_int(str):
    str = strip_character(str, ['(',')'])
    if not str:
        pass
    else:
        str = int(str)

    return str

def strip_character(str, bad_chars):
    for char in bad_chars:
        str = str.replace(char, '') 
    return str

with open('artworks.csv') as read_f, open('artworks_clean.csv', 'w') as write_f: 
   csv_reader = reader(read_f)
   csv_writer = writer(write_f)
   try:
       while True:
           line = next(csv_reader)
           if csv_reader.line_num == 1:
               csv_writer.writerow(line)
           else:
               handle_rows(line)
               #csv_writer.writerow(handle_rows(line))
               csv_writer.writerow(line)
   except StopIteration:
       print('handle complete')


     
  # rows = list(csv_reader)
  # for row in rows:
  #     nationality = row[2] #Nationality
  #     beginDate = row[3]
  #     endDate = row[4]
  #     gender = row[5]
  #     date = row[6]

       

       
