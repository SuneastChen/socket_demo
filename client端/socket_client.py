import socket
host='192.168.0.148'
port=50000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #s为套接字(服务器间网络通信,for TCP流式socket)
s.connect((host,port))   #s套接字去连接服务器

s.sendall('hello world!'.encode('utf-8'))   #s套接字发送数据
received_data=s.recv(1024).decode('utf-8')   #s套接字接收数据
print('我接收返回的数据:',received_data)    #数据处理
s.close()   #关闭套接字
