#!/usr/bin/python3.4
# _*_ coding:utf-8 _*_

import socketserver    #linux中py2.7中用SocketServer,仅此特殊,而且不需要转码
class MyTCPHandler(socketserver.BaseRequestHandler):    #继承建类
    def handle(self):    #必须定义此函数,且函数名为handle(),被类绑定了,建立连接自处调取此方法
        self.data=self.request.recv(4096).decode('utf-8')   #接收,获得数据
        print(self.data)
        result=self.data.upper()   #数据处理
        self.request.sendall(result.encode('utf-8'))   #返回处理结果

host='' 
port=9999
server=socketserver.ThreadingTCPServer((host,port),MyTCPHandler)   #socketserver绑定地址,类 成为server实例
server.serve_forever()   #server实例 永远开启服务
