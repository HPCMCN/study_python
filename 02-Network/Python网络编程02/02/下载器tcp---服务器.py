import socket as s
import os
import time

# 创建一个socket
tcp_server = s.socket(s.AF_INET, s.SOCK_STREAM)
# 初始化端口
tcp_server.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, True)
# 设置服务
ip_port = ("", 8080)
tcp_server.bind(ip_port)
# 变主动为被动
tcp_server.listen(128)
print("服务已开启!")
# 死循环接受数据
while True:
    # 接收客户发来的信息:
    client_tcp, ip_port = tcp_server.accept()
    print("检测到用户 %s 接入" % str(ip_port))
    # 创建文件夹并打开
    while True:
        print("等待命令: ")
        client_msg = client_tcp.recv(1024).decode("gbk")
        if client_msg == "close":   # 用户输入lose 关闭信息传输
            client_tcp.close()
            # tcp_server.close()
            break
        elif client_msg == "ls":
            path = os.listdir(os.getcwd())  # 获取服务器本地列表
            client_tcp.send(str(path).encode("gbk"))
        elif client_msg[:2] == "下载":
            client_msg = client_msg[2:]
            print(client_msg)
            client_tcp.send('文件存在,正在读取并发送...'.encode("gbk"))
            try:
                with open("./test/" + client_msg, "rb") as f:
                    while True:
                        content = f.read(1024)
                        if content:
                            client_tcp.send(content)
                            time.sleep(0.2)
                        else:
                            print("文件传输完毕!")
                            client_tcp.send('文件传输完毕'.encode("gbk"))
                            break
            except Exception:
                client_tcp.send("文件读取错误, 请检查是否存在!".encode("gbk"))
        else:
            print("指令有误!")

