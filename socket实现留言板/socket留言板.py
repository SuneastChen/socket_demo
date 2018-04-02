import socket
from urllib.parse import unquote

# 打印参数功能
def log(*args,**kwargs):
    print(*args, **kwargs)



# 定义一个类用于储存请求的信息
class Request(object):
    def __init__(self):
        self.path = ''
        self.query = {}
        self.method = 'GET'
        self.body = ''

    def form(self):  # post提交的数据,处理,得到字典
        body = unquote(self.body)
        log('body是:', body)  # message=1&author=2
        args = body.split('&')
        f = {}
        for arg in args:
            k, v = arg.split('=')
            f[k] = v
        return f




# 定义一个Request实例,来储存请求信息  
request = Request()


# 获取路径和参数
def parsed_path(path):
    index = path.find('?')
    if index == -1:
        return path, {}
    else:
        path, query_s = path.split('?', 1)  # 参数1,代表只分割一次
        args = query_s.split('&')
        query = {}
        for arg in args:
            k, v = arg.split('=')
            query[k] = v
        return path, query











# 定义主页视图函数
def route_index():
    header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
    body = '<h1>Hello World!</h1>'
    r = header + '\r\n' + body
    return r.encode('utf-8')


# 定义 /shine 视图函数
def route_shine():
    header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
    body = '<h1>Hello World!</h1><img src="img/shine.gif"/>'
    r = header + '\r\n' + body
    return r.encode('utf-8')

def route_image_shine():
    with open('img/shine.gif', 'rb') as f:
        header = b'HTTP/1.1 200 OK\r\nContent-Type: image/gif\r\n'
        img = header + b'\r\n' + f.read()   # 注意用字节型的
        return img



# 定义 /meinv 视图函数
def route_meinv():
    header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
    body = '<h1>Hello World!</h1><img src="img/meinv.gif"/>'
    r = header + '\r\n' + body
    return r.encode('utf-8')


def route_image_meinv():
    with open('img/meinv.gif', 'rb') as f:
        header = b'HTTP/1.1 200 OK\r\nContent-Type: image/gif\r\n'
        img = header + b'\r\n' + f.read()   # 注意用字节型的
        return img

# 定义 /all 视图函数
def route_all():
    header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
    body = '<h1>Hello World!</h1><img src="img/shine.gif"/><img src="img/meinv.gif"/>'
    r = header + '\r\n' + body
    return r.encode('utf-8')




class Message(object):
    def __init__(self):
        self.message = ''
        self.author = ''
    def __repr__(self):
        return '{}:{}'.format(self.message, self.author)

message_list = []


def template(filename):
    with open('templates/'+filename, 'r', encoding='utf-8') as f:
        return f.read()




# 定义 /message 留言板功能 视图函数
def route_message():
    if request.method == 'POST':
        # 解析body参数
        msg = Message()
        form = request.form()  # form是个字典
        print(form)
        # 分别存储信息
        msg.author = form.get('author', '')
        msg.message = form.get('message', '')
        message_list.append(msg)
        print(message_list)

    header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
    body = template('message.html')
    msgs = '<br>'.join([str(m) for m in message_list])
    body = body.replace('{{message}}', msgs)
    r = header + '\r\n' + body
    return r.encode('utf-8')













def error(code=404):
    error_dict = {
        404: b'HTTP/1.1 404 NOT FOUND\r\n<h1>404 NOT FOUND</h1>',
        405: b''
    }
    return error_dict.get(code, b'')



# 处理路径,返回响应数据
def response_for_path(path):
    path, query = parsed_path(path)
    request.path = path
    request.query = query
    log('path and query:', path, query)
    # 定义路由
    r = {
        '/': route_index,  # 需要定义一个视图函数
        '/shine': route_shine,
        '/meinv': route_meinv,
        '/all': route_all,

        '/img/shine.gif': route_image_shine,
        '/img/meinv.gif': route_image_meinv,

        '/message': route_message
    }

    response = r.get(path,error)  # 需要定义error的类型
    return response()  # 返回视图函数的执行




def run(host='',port=3000):
    # 创建一个socket实例
    # s = socket.socket()
    with socket.socket() as s:
        s.bind((host,port))  # s实例绑定服务器host和port
        while True:
            s.listen(3)
            connection, address = s.accept()
            r = connection.recv(1024)
            # 将传输的bytes类型数据,转换成 str
            r =r.decode('utf-8')  

            # GET /message?message=1&author=2 HTTP/1.1
            try:
                request.method = r.split()[0]
                request.body = r.split('\r\n\r\n')[1]
                path = r.split()[1]
                # 根据用户给的path,给一个函数处理,返回响应数据
                response = response_for_path(path)
                # 将响应数据 发送给客户端
                connection.sendall(response)
            except Exception as e:
                log('error', e)
            # 关闭与客户端连接
            connection.close()


if __name__ == '__main__':
    config = dict(host='', port=3000)
    run(**config)