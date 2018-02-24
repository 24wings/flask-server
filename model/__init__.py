#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql
connection  = pymysql.connect(host="localhost",user="root",password="root",db="cmswing" )
# 使用cursor()方法获取操作游标 

# SQL 查询语句
sql = "SELECT * FROM cmswing.actions"
try:

    with connection.cursor() as cursor:
        # Read a single record
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()