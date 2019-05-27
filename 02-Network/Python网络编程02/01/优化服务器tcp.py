import socket as s
import time
import threading as t
import os


class TestException(Exception):
    """自定义错误类型"""
    def __init__(self, error):
        self.error = error


def load_date(client_date):
    """下载"""
    # 字符串拼接成绝对路径, 二进制打开文件, 发送到客户端
    try:
        print("获取文件: %s 中...." % str(client_date))
        with open("./" + client_date, "rb") as rf:
            client_socket.send("下载中, 请稍后...".encode("gbk"))
            i = 0
            while True:
                content = rf.read(1024)
                if content:
                    client_socket.send(content)
                    # 每次发送让服务器先等个几秒, 给客户端喘口气
                    time.sleep(0.3)
                    print(i)
                    i += 1
                else:
                    print("文件下载完毕!")
                    print_msg("文件下载完毕!")
                    break
    except FileNotFoundError:
        error_msg("当前路径不存在此文件!")
    except Exception:
        error_msg("下载失败!")


def uploading_date(client_date):
    """上传"""
    try:
        print("创建文件: %s 中...." % str(client_date))
        with open("./" + client_date, "wb") as wf:
            print("正在创建链接,请稍后...")
            i = 0
            while True:
                content = client_socket.recv(1024)
                if "完成".encode("gbk") not in content:
                    wf.write(content)
                    # 客户端慢点, 让服务器喘口气
                    time.sleep(0.1)
                    print(i)
                    i += 1
                else:
                    print("文件上传完毕")
                    break
    except Exception:
        error_msg("上传失败!")


def print_msg(p_msg):
    """客户端需要打印的信息"""
    client_socket.send(p_msg.encode("gbk"))


def send_date(list_dir):
    """发送目录列表"""
    client_socket.send(list_dir.encode("gbk"))


def error_msg(error):
    """错误信息数据开头加0"""
    client_socket.send(("0" + error).encode("gbk"))


def decode_date():
    """数据处理"""
    # 循环接收数据并转码成gbk,同时切除第一位, 若在1, 2, 3, 4中执行 否则直接抛出异常,并发送给客户端
    while True:
        client_msg = client_socket.recv(1024).decode("gbk")
        try:
            if "关闭" in client_msg:
                client_socket.close()
                break
            elif client_msg[:1] not in ["1", "2", "3"]:
                raise TestException("输入有误, 请确认后重试!")
            else:
                # 满足条件进行下次跳转, 否则直接发送异常至客户端
                if deal_date(client_msg):
                    break
        except TestException as error:
            print(type(error))
            error_msg(error)


def deal_date(client_msg):
    cmd = client_msg[:1]
    client_msg = client_msg[1:]
    client_socket.send("处理中,请稍后...".encode("gbk"))
    time.sleep(0.3)
    if cmd == "1":
        # 获取当前文件信息并发送给客户端
        print("对方正在获取本地目录")
        list_dir = os.listdir(os.getcwd())
        send_date(str(list_dir))
    elif cmd == "2":
        # 调用下载端口
        print("对方准备下载:" + client_msg)
        load_date(client_msg)
        return True
    else:
        # 调用上传端口
        print("对方准备上传:" + client_msg)
        uploading_date(client_msg)
        return True
    return False


if __name__ == '__main__':
    # 创建套接字:
    tcp_serve = s.socket(s.AF_INET, s.SOCK_STREAM)
    # 端口重载:
    tcp_serve.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, True)
    # 绑定端口:
    print("*" * 20, "TCP服务器", "*" * 20)
    print("请输入本地IP及端口: ")
    try:
        serve_ip_port = (input("  IP:"), int(input("端口: ")))
        tcp_serve.bind(serve_ip_port)
    except Exception:
        print("错误: 请输入正确的IP及端口!")
    # 变被动:
    tcp_serve.listen(128)
    print("服务启动成功!")
    while True:
        # 无限接收客户端连接(暂不设置退出!!!):
        client_socket, client_ip_port = tcp_serve.accept()
        print("用户 %s 已接入" % str(client_ip_port))
        try:
            cs = t.Thread(target=decode_date)
            cs.start()
        finally:
            # 让程序休息一会
            time.sleep(2)
