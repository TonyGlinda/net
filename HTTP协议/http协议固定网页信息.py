import socket


def rec_msg(new_tcp_socket):
    msg = new_tcp_socket.recv(1024)
    print(msg)
    respond = 'HTTP/1.1 200 ok \n'
    respond += '\n'
    respond += '<h1>hahahha</h1>'
    new_tcp_socket.send(respond.encode('gbk'))


def main():
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_socket.bind(('',8080))
    tcp_socket.listen(128)
    new_tcp_socket,client_addr = tcp_socket.accept()
    rec_msg(new_tcp_socket)
    new_tcp_socket.close()
    tcp_socket.close()



if __name__=='__main__':
    main()
