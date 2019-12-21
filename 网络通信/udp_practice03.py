import socket


def sendto_msg(udp_socket):

    msg = input('请输入要发送的信息： ')
    desk_ip = input('请输入目标ip： ')
    desk_port = int(input('请输入目标的端口： '))
    udp_socket.sendto(msg.encode('gbk'),(desk_ip, desk_port))
    udp_socket.close()


def rec_msg(udp_socket):
    address = ('',8080)
    udp_socket.bind(address)
    msg = udp_socket.recvfrom(65536)
    print(msg[0].decode('gbk'))
    udp_socket.close()


while True:
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('............')
    print('请输入你要选的功能')
    print('1.发送消息')
    print('2.接收消息')
    print('0.退出系统')
    op = input('请选择你要选的功能： ')
    if op == '1':
        sendto_msg(udp_socket)
    elif op == '2':
        rec_msg(udp_socket)
    elif op == '0':
        break
    else:
        print('输入错误，请重新输入！')
