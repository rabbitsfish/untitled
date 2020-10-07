import socket

def send_msg(udp_socket):
    host = input('请输入ip地址：')
    port = int(input('请输入端口号：'))
    msg = input('请输入你要说的话')
    udp_socket.sendto(msg.encode('gbk'), (host, port))

def receive_msg(udp_socket):
    print('receive_msg')
    recv_msg = udp_socket.recvfrom(1024)
    print(recv_msg)
    print('%s:%s' % (recv_msg[1], recv_msg[0].decode('gbk')))

if __name__ == '__main__':
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('', 2389))

    while True:
        menu_id = input('请输入菜单选项:/r')
        if menu_id == '1':
            send_msg(udp_socket)
        elif menu_id == '2':
            receive_msg(udp_socket)
        else:
            print('error')