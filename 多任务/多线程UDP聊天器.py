import socket,threading


def sendto_msg(udp_socket):
    dest_ip = input('请输入对方的ip： ')
    dest_port = int(input('请输入对方的port：'))
    while True:
        msg = input('请输入要发送的信息：')
        if msg:
            udp_socket.sendto(msg.encode('gbk'),(dest_ip,dest_port))
        else:
            break





def recvfrom_msg(udp_socket):
    while True:
        msg = udp_socket.recvfrom(1024)
        print(msg[0].decode('gbk'))



def main():
    # 创建UDP套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定端口
    udp_socket.bind(('',8080))
    t1 = threading.Thread(target=sendto_msg, args=(udp_socket,))
    t2 = threading.Thread(target=recvfrom_msg,args=(udp_socket,))
    # 发送信息
    t1.start()
    t2.start()
    # 接收信息


if __name__ =='__main__':
    main()
