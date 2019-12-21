import socket


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 创建套接字
    tcp_socket.connect(('192.168.199.209', 8080)) # 链接服务器
    download_file = input('请输入要下载文件的名字： ')  # 获取要下载的文件名字。
    tcp_socket.send(download_file.encode('gbk')) # 发送文件名到服务器
    date_file = tcp_socket.recv(1024*1024) # 接收服务器文件内容 1M
    with open('[新]'+ download_file, 'wb') as f: # 创建文件写入数据
        f.write(date_file)
        f.close()
    tcp_socket.close()  # 关闭套接字


if __name__ == '__main__':
    main()
