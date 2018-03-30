#!/usr/bin/env python
# coding:utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import MySQLdb
import MySQLdb.cursors

db = MySQLdb.connect(host='localhost', user='root', passwd='CS197680626', db='douban', port=3306, charset='utf8', cursorclass = MySQLdb.cursors.DictCursor)
db.autocommit(True)
cursor = db.cursor()

fr = open('douban_movie_clean.txt','r')

# #Create
# count = 0
# for line in fr:
#     count += 1
#     print count
#     if count == 1:
#         continue
#
#     line = line.strip().split('^')
#     cursor.execute("insert into movies(title,url,rate,length,description)values(%s,%s,%s,%s,%s)",[line[1],line[2],line[4],line[-3],line[-1]])
#
# fr.close()

#Update
# cursor.execute("Update movies set title=%s,length=%s where id=1",['Miss思',999])

#Read
# cursor.execute("select title,length from movies where id=1")
# movies = cursor.fetchall()

#Delete
cursor.execute("delete from movies where id=%s",[1])

cursor.close()
db.close()