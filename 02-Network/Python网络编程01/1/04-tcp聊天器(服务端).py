import socket


def main():
    """主程序入口"""
    # 1. 创建一个本地服务器
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 设置本地连接
    tcp_server.bind(("", int(input("请输入端口: "))))
    # 3. 设置最大连接数量
    tcp_server.listen(128)

    # 4. 接受对方传来数据  并进行拆包
    client_server, client_ip_port = tcp_server.accept()
    print("连接成功!")
    print(client_ip_port)
    # 5. 创建死循环获取并发送信息
    while 3:
        client_msg = client_server.recv(1024).decode("utf-8")
        print(client_msg)
        client_send = client_server.send((input("请输入要发送的信息: ") + "\n").encode("utf-8"))
        # 6. 如果不在输入信息就直接程序结束
        if client_send == "\n".encode("utf-8"):
            client_server.close()
            tcp_server.close()
            break


if __name__ == '__main__':
    main()
