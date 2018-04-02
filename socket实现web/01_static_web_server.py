# _*_ coding:utf-8 _*_
# !/usr/bin/python

import socket
from multiprocessing import Process

# tcp socket 服务端
HTML_ROOT_DIR = ''


def handle_client(client_socket):
    """处理客户端请求函数"""
    # 获取客户端请求数据
    request_data = client_socket.recv(1024)
    print('request data:', request_data)

    # 构造响应数据
    response_start_line = 'HTTP/1.1 200 OK\r\n'
    response_headers = 'Server:My server\r\n'
    response_body = 'hello world!'
    response = response_start_line + response_headers + '\r\n' + response_body
    print('response data:', response)

    # 向客户端返回响应数据
    client_socket.send(response.encode('utf_8'))
    # 关闭客户端连接
    client_socket.close()


if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", 8000))  # 用元组形式
    server_socket.listen(128)

    while 1:
        client_socket, client_address = server_socket.accept()
        print('[%s,%s]用户连接上了' % client_address)  # client_address是个IP,端口的元组
        handle_client_process = Process(target=handle_client, args=(client_socket,))
        handle_client_process.start()
        client_socket.close()
