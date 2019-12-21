import socket
def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    local_addr = ('',60601) # IP地址一般可以不写，表示本机的一个任意地址。
    s.bind(local_addr) # 绑定固定端口，必须绑定自己的IP和端口。
    rec_messages = s.recvfrom(1024) # 等待接收对方发送的数据。1024表示最大字节数。
    print(rec_messages[0].decode('gbk'))  # rec_messages 是一个元组，使用decode解码。
    s.close()
if __name__ == '__main__':
    main()

