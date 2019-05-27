import socket

if __name__ == '__main__':
    # 创建套接字
    utp_ip_port = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 创建ip_port  创建服务器
    ip_port = "", int(input("端口: "))
    utp_ip_port.bind(ip_port)
    # 接收+ 解包
    msg, slt_ip_port = utp_ip_port.recvfrom(1024)
    print(msg.decode("utf-8"))
    utp_ip_port.sendto(input("信息: ").encode("utf-8"), slt_ip_port)
    # 关闭端口
    utp_ip_port.close()
