#!/usr/bin/python
# _*_ coding:utf-8 _*_

import MySQLdb

#创建数据库,创建表
try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123123',port=3306)
    cur=conn.cursor()
    cur.execute('create database if not exists test2')
    conn.select_db('test2')
    cur.execute('create table host(host varchar(20),user varchar(10),passwd varchar(20));')
    value=['10.0.0.29','alex','123']
    cur.execute('insert into host values(%s,%s,%s);',value)
    conn.commit()
    cur.close()
    conn.close()
except MySQLdb.Error as e:
    print('Mysql Error Msg:',e)
    
