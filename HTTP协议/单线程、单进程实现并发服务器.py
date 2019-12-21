import socket
import time


def main():
    # 创建tcp套接字
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_socket.setblocking(False) # 将套接字设置为非阻塞的
    # 绑定套接字
    tcp_socket.bind(('',8080))
    # 监听套接字
    tcp_socket.listen(128)
    # 等待客户端的连接
    socket_client_list = list()
    while True:
        try:
            new_tcp_socket, client_addr = tcp_socket.accept()
            socket_client_list.append(new_tcp_socket)
        except:
            # time.sleep(1)
            print('----没有新的客户端到来----')
        else:
            new_tcp_socket.setblocking(False)
        for i in socket_client_list:
            try:
                msg = i.recv(1024)
            except:
                print('=======没有新的信息发送过来=====')
            else:
                if msg:
                    print(msg.decode('gbk'))
                else:
                    tcp_socket.close()
                    socket_client_list.remove(i)


if __name__=='__main__':
    main()



