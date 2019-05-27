import socket


def main():
    """主函数"""
    # 创建套接字
    tcp_ip_port = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 创建ip_port, 连接服务器
    ip_port = input("IP: "), int(input("端口: "))
    tcp_ip_port.connect(ip_port)
    print("连接成功!")
    tcp_ip_port.send(input("发送: ").encode("utf-8"))
    msg = tcp_ip_port.recv(1204)
    print(msg.decode("utf-8"))
    tcp_ip_port.close()


if __name__ == '__main__':
    main()