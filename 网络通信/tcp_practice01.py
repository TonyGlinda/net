import socket


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 建立套接字
    service_ip = input('请输入要链接的ip: ')
    service_port = int(input('请输入要链接的port: '))
    tcp_socket.connect((service_ip, service_port))  # 链接服务器
    while True:
        msg = input('请输入要发送的信息： ')  # 发送信息给服务器
        if msg:
            tcp_socket.send(msg.encode('gbk'))
            date = tcp_socket.recv(1024)
            print(date.decode('gbk'))
        else:
            tcp_socket.close()  # 关闭套接字。
            break


if __name__ == '__main__':
    main()


