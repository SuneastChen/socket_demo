#!/usr/bin/python
# _*_ coding:utf-8 _*_

import MySQLdb
try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123123',db='test',port=3306) #建立连接
    cur=conn.cursor()    #指定当前光标
    cur.execute('select * from students;')   #执行代码
    result=cur.fetchall()   #获取执行结果对象
    for line in result:
        print line
    cur.close()    #关闭当前光标
    conn.close()   #关闭连接
except MySQLdb.Error as e:
    print('Mysql Error Msg:',e)
    
