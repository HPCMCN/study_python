import socket

if __name__ == '__main__':
    # 创建套接字
    tcp_ip_port = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 创建服务器ip,端口
    ip_port = "", int(input("端口: "))
    tcp_ip_port.bind(ip_port)
    # 变主动为被动
    tcp_ip_port.listen(128)
    # 等待用户接入
    client_socket, client_ip_port = tcp_ip_port.accept()

    # 接收信息  加解包
    msg = client_socket.recv(1024)
    print(msg.decode("utf-8"))
    # 发送信息
    client_socket.send(input("发消息: ").encode("utf-8"))
    # 关闭用户端和服务器
    client_socket.close()
    tcp_ip_port.close()
