import socket


def main():
    """主函数"""
    # 创建套接字
    tcp_ip_port = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 创建默认ip_port
    ip_port = "", int(input("端口: "))
    tcp_ip_port.bind(ip_port)
    # 变主动为被动
    tcp_ip_port.listen(128)
    # 创建连接 并拆包
    client_socket, client_ip_port = tcp_ip_port.accept()
    print("有新用户接入!")

    while 2:
        # 接收并拆包
        msg1 = client_socket.recv(1024)
        print(msg1.decode("utf-8"))
        # 发送并转码
        client_socket.send(input("发送: ").encode("utf-8"))
    # 故意放外面的  就是不让他跳出来
    client_socket.close()
    tcp_ip_port.close()


if __name__ == '__main__':
    main()