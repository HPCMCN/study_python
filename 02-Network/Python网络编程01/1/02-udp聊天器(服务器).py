import socket


def main():
    """主函数"""
    #  1 创建套接字
    udp_ip_port = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #  2 设置服务器IP_port
    udp_ip_port.bind((input("本地IP: "), int(input("端口: "))))
    while 1:
        #  3 接收信息并拆包成msg, ip-port
        client_msg, ip_port = udp_ip_port.recvfrom(1024)
        print(client_msg.decode("utf-8"))
        if client_msg.decode("utf-8") == "关闭":  # 用户输入关闭后, 关闭服务器
            udp_ip_port.close()
            break
        #  4 发送信息
        udp_ip_port.sendto((input("请输入发送的信息: ")+"\n").encode("utf-8"), ip_port)


if __name__ == '__main__':
    main()
