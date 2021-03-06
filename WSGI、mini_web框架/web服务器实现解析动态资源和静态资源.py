import socket
import multiprocessing
import re
import time


class WebServer(object):
    def __init__(self):
        """实现简单的HTTP服务器，发送固定信息"""
        # 创建TCP套接字
        self.tcp_socket_server = socket.socket(socket.AF_INET,
                                               socket.SOCK_STREAM)
        # 自动使用上次的端口
        self.tcp_socket_server.setsockopt(socket.SOL_SOCKET,
                                          socket.SO_REUSEADDR, 1)
        # 绑定套接字
        self.tcp_socket_server.bind(('', 8080))
        # 监听套接字
        self.tcp_socket_server.listen(128)

    @staticmethod
    def server_for_recv(new_tcp_socket):
        request = new_tcp_socket.recv(1024).decode('utf8')
        request_lines = request.splitlines()
        for temp in request_lines:
            print(temp)
        rlt = re.search(r'/.*\s', request_lines[0])
        file_name = ''
        if rlt:
            file_name = rlt.group()
            if file_name == '/ ':
                file_name = '/index.html'
        if not file_name.endswith(".py "):
            try:
                f = open('./html' + file_name, 'rb')
            except:
                header = 'HTTP/1.1 200 ok \r\n'
                header += '\r\n'
                header += '<h1>404 NOT FOUND</h1>'
                new_tcp_socket.send(header.encode('gbk'))
            else:
                contents = f.read()
                header = 'HTTP/1.1 200 ok \r\n'
                header += '\r\n'
                new_tcp_socket.send(header.encode('gbk'))
                new_tcp_socket.send(contents)
        else:
            header = 'HTTP/1.1 200 ok \r\n'
            header += '\r\n'
            header += '<h1>现在的时间是%s</h1>'% time.ctime()
            new_tcp_socket.send(header.encode('gbk'))

    def main(self):
        while True:
            # 等待客户端的链接，并创建新的套接字为这个客户端服务！
            new_tcp_socket, client_address = self.tcp_socket_server.accept()
            p1 = multiprocessing.Process(target=self.server_for_recv,
                                         args=(new_tcp_socket, ))
            p1.start()
            new_tcp_socket.close()


def main():
    web_server = WebServer()
    web_server.main()


if __name__ == '__main__':
    main()
