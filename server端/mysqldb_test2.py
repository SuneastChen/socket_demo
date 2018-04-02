#!/usr/bin/python
# _*_ coding:utf-8 _*_

import MySQLdb
try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123123',port=3306)  #无db参数
    cur=conn.cursor()
    cur.execute('create database if not exists test3')   #执行创建数据库
    conn.select_db('test3')   #use test3
    cur.execute('create table host(host varchar(20),user varchar(10),passwd varchar(20));')  #执行创建字段
    value=[]
    for i in range(20):
        ip='10.0.0.%s' % i
        value.append((ip,'alex','%s%s%s'%(i,i,i)))    #预先生成value,元组的列表
    
    cur.executemany('insert into host values(%s,%s,%s);',value)    #用executemany多次执行
    conn.commit()   #连接提交
    print('执行_提交  success！')
    cur.close()
    conn.close()
except MySQLdb.Error as e:
    print('Mysql Error Msg:',e)
    
