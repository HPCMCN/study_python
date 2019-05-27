import socket


def main():
    """主函数"""
    # 1 创建套接字
    udp_ip_port = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2 创建发送服务器ip_port
    client_ip_port = input("IP: "), int(input("端口"))
    while 1:
        client_msg = input("发送: ")
        if client_msg == "":
            break
        udp_ip_port.sendto(client_msg.encode("utf-8"), client_ip_port)
        # 3 接收服务器信息
        serve_msg, ip_port = udp_ip_port.recvfrom(1024)
        print(serve_msg.decode("utf-8"))
        # 4 关闭客户端
    udp_ip_port.close()


if __name__ == '__main__':
    main()
