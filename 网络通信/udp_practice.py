import socket
def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    messages = input('请输入发送的信息： ')
    s.sendto(messages.encode('utf_8'),('192.168.199.155',8080))
if __name__ == '__main__':
    main()

