import socket


def main():
    """主函数"""
    # 创建套接字
    udp_ip_port = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 创建本地ip_port  并设置服务器
    ip_port = "", int(input("端口: "))
    udp_ip_port.bind(ip_port)

    client_msg, client_ip_port = udp_ip_port.recvfrom(1024)
    print(client_msg.decode("gbk"))
    udp_ip_port.sendto(input("请输入: ").encode("utf-8"), client_ip_port)
    udp_ip_port.close()


if __name__ == "__main__":
    main()