import socket


def main():
    """主程序入口"""
    # 1. 创建一个套接字
    tcp_ip_port = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 创建连接
    opi = input("请输入连接IP: "), int(input("请输入端口"))
    tcp_ip_port.connect(opi)
    print("连接成功!")
    # 3. 发送和接受
    while 1:
        send_word = input("请输入发送的内容: ") + "\n"
        if send_word == "\n":
            break
        tcp_ip_port.send(send_word.encode("utf-8"))
        msg = tcp_ip_port.recv(1024).decode()
        print(msg)


if __name__ == '__main__':
    main()
