# _*_ coding:utf-8 _*_
# !/usr/bin/python

import socket
from multiprocessing import Process
import re

# 设置静态文件根目录
HTML_ROOT_DIR = './html'


def handle_client(client_socket):
    """处理客户端请求函数"""
    # 获取客户端请求数据
    request_data = client_socket.recv(1024)
    print('request data:', request_data)  # 接下来需要解析字符串
    request_lines = request_data.splitlines()
    request_start_line = request_lines[0]  # GET / HTTP/1.1
    # 提取用户请求的文件名
    file_name = re.match(r'\w+ +(/.*?) ', request_start_line.decode('utf-8')).group(1)
    print('file_name:%s' % file_name)

    # 打开文件,读取内容,构造响应数据
    try:
        with open(HTML_ROOT_DIR + file_name, 'rb') as f:
            file_data = f.read()
            # 用file_data去替换respons_body的内容
    except IOError:
        response_start_line = 'HTTP/1.1 404 Not Found\r\n'
        response_headers = 'Server:My server\r\n'
        response_body = '你请求的文件不存在!'
    else:
        # 构造响应数据
        response_start_line = 'HTTP/1.1 200 OK\r\n'
        response_headers = 'Server:My server\r\n'
        response_body = file_data.decode('utf-8')

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

        # 设置下端口不能重用的问题,(设置的级别,设置的是重用地址,True)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        print('[%s,%s]用户连接上了' % client_address)  # client_address是个IP,端口的元组
        handle_client_process = Process(target=handle_client, args=(client_socket,))
        handle_client_process.start()
        client_socket.close()
