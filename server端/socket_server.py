#!/usr/bin/python2.7
# _*_ coding:utf-8 _*_

#py2.7不用转码
import socket
host=''
port=50000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)    #s为套接字(服务器间网络通信,for TCP流式socket)
s.bind((host,port))   #将s套接字绑定ip地址,在端口
s.listen(2)    #开始监听,接受客户端的连接
while 1:
    conn,addr=s.accept()   #接受了连接,并且返回conn对象和addr地址

    print('我被lian接了，IP地址是：',addr)
    data=conn.recv(4096)   #conn对象接收数据
    print('接收到数据：',data)
    if not data:
        #break     #一直处于接收数据状态
        time.sleep(2)    #服务器睡0.5秒很有必要
    result=data.upper()   #数据处理
    conn.sendall(result)  #conn对象发送数据
#conn.close()    #不用可以关闭
