import socket
import threading


def server_for_recv(new_tcp_socket):
    request = new_tcp_socket.recv(1024)
    request_lines = request.splitlines()
    for temp in request_lines:
        print(temp)
    header = 'HTTP/1.1 200 ok \r\n'
    header += '\r\n'
    body = '<h1>已经成功链接服务器！</h1>'
    respond = header + body
    new_tcp_socket.send(respond.encode('gbk'))


def main():
    """实现简单的HTTP服务器，发送固定信息"""
    # 创建TCP套接字
    tcp_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 自动使用上次的端口
    tcp_socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定套接字
    tcp_socket_server.bind(('', 8080))
    # 监听套接字
    tcp_socket_server.listen(128)
    while True:
        # 等待客户端的链接，并创建新的套接字为这个客户端服务！
        new_tcp_socket, client_address = tcp_socket_server.accept()
        t1 = threading.Thread(target=server_for_recv,
                                     args=(new_tcp_socket,))
        t1.start()
        #new_tcp_socket.close()


if __name__ == '__main__':
    main()
