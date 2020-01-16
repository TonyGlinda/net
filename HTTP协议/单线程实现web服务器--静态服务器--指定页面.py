import socket
import re


def server_for_client(new_tcp_socket):
    request = new_tcp_socket.recv(1024).decode('utf8')
    request_lines = request.splitlines()
    for temp in request_lines:
        print(temp)
    # 利用正则表达式获取header   GET ./html/index.html http/1.1
    rlt = re.search(r'index|(/[^ ]*)', request_lines[0]) # 匹配/ 或者/index.html
    file_name = ''
    if rlt:
        file_name = rlt.group()
        if file_name == '/':
            file_name = '/index.html'
    try:
        f = open(r'./html'+file_name, 'rb')

    except:
        header = 'HTTP/1.1 404 NOT FOUND \r\n'
        header += '\r\n'
        body = '<h1>NOT FOUND 404</h1>'
        respond = header + body
        new_tcp_socket.send(respond.encode('utf8'))

    else:
        contents = f.read()
        # 服务器发送header和body给客户端
        header = 'HTTP/1.1 200 ok \r\n'
        header += '\r\n'
        body = contents
        respond = header
        new_tcp_socket.send(respond.encode('utf8'))
        new_tcp_socket.send(body)


def main():
    """实现简单的HTTP服务器，发送固定信息"""
    # 创建TCP套接字
    tcp_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定套接字
    tcp_socket_server.bind(('', 8080))
    # 监听套接字
    tcp_socket_server.listen(128)
    while True:
        # 等待客户端的链接，并创建新的套接字为这个客户端服务！
        new_tcp_socket, client_address = tcp_socket_server.accept()
        server_for_client(new_tcp_socket)
        new_tcp_socket.close()


if __name__ == '__main__':
    main()
