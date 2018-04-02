import socket
import time
host='192.168.0.148'
port=9999
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

while 1:
	inp=input('write command:')
	s.sendall(inp.encode('utf-8'))
	received_data=s.recv(1024).decode('utf-8')
	time.sleep(2)
	print('我接收到返回的数据:',received_data)
s.close()