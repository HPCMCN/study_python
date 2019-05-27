import socket
# 创建一个socket
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置本地IP 端口
try:
    ip_port = input("IP"), int(input("端口"))
except:
    print("请输入正确的端口: 1024~65535")
# 连接服务器
else:
    try:
        tcp_client.connect(ip_port)
    except:
        print("连接失败")
    while True:
        cmd = input("请输入: ")
        tcp_client.send(cmd.encode("utf-8"))

        sever_msg = tcp_client.recv(1024)
        if "错误" not in sever_msg and cmd == "ls":
            with open("./test/" + cmd, "rb") as f1:
                while True:
                    sever_msg = tcp_client.recv(1024)
                    if sever_msg:
                        f1.write(sever_msg)
                    else:
                        break
        else:
            print(sever_msg)