#!/usr/bin/python3.4
# _*_ coding:utf-8 _*_

import socketserver    #linux中py2.7中用SocketServer,仅此特殊,而且不需要转码
import os
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):     #必须定义此函数,且函数名为handle(),被绑定了
        print('我被lian接了，ip地址是：',self.client_address)
        while 1:
            self.data=self.request.recv(4096).decode('utf-8')
            print(self.data)
            cmd=os.popen(self.data)
            result=cmd.read()
            self.request.sendall(result.encode('utf-8'))

host='' 
port=9999
server=socketserver.ThreadingTCPServer((host,port),MyTCPHandler)
server.serve_forever()
