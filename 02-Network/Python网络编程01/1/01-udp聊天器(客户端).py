import socket


def main():
    """主函数"""
    #  1.创建一个流对象
    udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #  2. 创建对方信息  并发送
    ip_port = input("IP "), int(input("端口: "))
    while 1:
        client_msg = input("输入发送信息: " + "\n").encode("utf-8")
        udp_client.sendto(client_msg, ip_port)
        #  3. 接受对方信息  解码
        msg, ip_port2 = udp_client.recvfrom(1024)
        print(msg.decode("utf-8"))


if __name__ == '__main__':
    main()
