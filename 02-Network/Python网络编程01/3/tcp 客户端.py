import socket

if __name__ == '__main__':
    # 创建套接字
    tcp_ip_port = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 创建服务器连接
    ip_port = input("IP: "), int(input("端口: "))
    tcp_ip_port.connect(ip_port)
    print("连接成功!")
    # 发送信息
    tcp_ip_port.send(input("发消息: ").encode("utf-8"))
    # 接收信息  加解包
    msg = tcp_ip_port.recv(1024)
    print(msg.decode("utf-8"))
    # 关闭
    tcp_ip_port.close()

