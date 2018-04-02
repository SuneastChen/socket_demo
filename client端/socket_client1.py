import socket
import time
host='192.168.0.148'
port=50000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

n=0
while n<10:
	n += 1
	s.sendall('hello world!'.encode('utf-8'))
	received_data=s.recv(1024).decode('utf-8')
	time.sleep(2)
	print('我接收到返回的数据:',received_data)
s.close()