import socket


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 创建套接字
    tcp_socket.bind(('', 8080)) # 绑定服务器
    tcp_socket.listen(128) # 监听
    new_socket, client_addr = tcp_socket.accept()
    new_socket.send('你已经链接服务器，请继续！'.encode('utf8'))
    while True:
        message = new_socket.recv(1024)
        if message:
            print(message.decode('utf8'))
        else:
            print('该用户已经退出服务器链接')
            new_socket.close()
            break
    tcp_socket.close()





if __name__ == '__main__':
    main()
