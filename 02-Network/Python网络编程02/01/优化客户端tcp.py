import socket as s
import time


def load_date(file):
    """下载"""
    # 字符串拼接成绝对路径, 二进制打开文件, 发送到客户端
    with open("./" + file, "wb") as wf:
        i = 1
        print(tcp_client.recv(1024).decode("gbk"))
        while True:
            content = tcp_client.recv(1024)
            if "文件下载完毕!".encode("gbk") not in content:
                wf.write(content)
                # 客户端慢点, 让服务器喘口气
                time.sleep(0.1)
                print(i)
                i += 1
            elif "失败".encode("gbk") in content:
                print(content.encode("gbk"))
            else:
                print("文件下载完毕")
                tcp_client.close()
                return False


def uploading_date(client_date):
    """上传"""
    with open("./" + client_date, "rb") as rf:
        i = 0
        time.sleep(0.5)
        while True:
            content = rf.read(1024)
            if content:
                tcp_client.send(content)
                # 每次发送让服务器先等个几秒, 给客户端喘口气
                time.sleep(0.3)
                print(i)
                i += 1
            else:
                print("文件下载完毕!")
                tcp_client.send("文件传送完成！".encode("gbk"))
                tcp_client.close()
                return False


def receive():
    """接收数据并进行处理"""
    while True:
        service_msg = tcp_client.recv(1024)
        cmd_num = service_msg[:1]
        # print(cmd, "\n")
        print(service_msg.decode("gbk"), "\n")
        if cmd_num == "0":
            return True
        if cmd == "1":
            print(tcp_client.recv(1024).decode("gbk"))
        if cmd == "2":
            print("准备中1...")
            print(file)
            return load_date(file)
        elif cmd == "3":
            print("准备中2...")
            print(file)
            return uploading_date(file)
        else:
            return True


if __name__ == '__main__':
    while True:
        # 创建套接字:
        tcp_client = s.socket(s.AF_INET, s.SOCK_STREAM)
        # 设置ip_port
        serve_ip_port = ("192.168.65.77", 8888)
        # 创建连接:
        tcp_client.connect(serve_ip_port)
        print("服务器连接成功!")
        # 进行数据加工
        while True:
            print("*" * 20, "tcp客户端", "*" * 20)
            print("1.查看服务器列表\n2.下载\n3.上传\n4.重连服务器")
            cmd = input("请输入: ")
            if cmd == "2":
                file = input("请输入下载文件名： ")
                cmd_date = "2" + file
            elif cmd == "3":
                file = input("请输入上传文件名： ")
                cmd_date = "3" + file
            elif cmd == "4":
                try:
                    tcp_client.send("关闭通讯！".encode('gbk'))
                    tcp_client.close()
                finally:
                    break
            else:
                cmd_date = cmd
            # 发送选项
            tcp_client.send(cmd_date.encode("gbk"))
            # 接收数据
            if receive() is False:
                break
            else:
                continue
