# coding:utf-8
import socket
import re
from multiprocessing import Process


def handle_client(client_socket):
    """返回浏览器数据"""
    request_date = client_socket.recv(1024)
    # print(request_date)
    request = re.search(r"/[^ ]*", request_date.decode()).group()
    print(request)
    if "/index.html" == request:
        with open("./download/baidu.html", "rb") as f:
            while True:
                content = f.read(1024)
                if content:
                    client_socket.send(content)
                else:
                    print("信息传送完毕!")
                    break
    elif "/" == request:
        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_headers = "Server: My server\r\n"
        response_body = "hello world!"
        response = response_start_line + response_headers + "\r\n" + response_body
        client_socket.send(response.encode())
        print("hello world!")
    else:
        response_start_line = "HTTP/1.1 404 Not Found\r\n"
        response_headers = "Server: My server\r\n"
        response_body = "文件定位失败!"
        print("失败!")
        response = response_start_line + response_headers + "\r\n" + response_body
        client_socket.send(response.encode("gbk"))
    client_socket.close()


if __name__ == '__main__':
    # 创建服务器
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    ip_port1 = ("", 80)
    server_socket.bind(ip_port1)
    server_socket.listen(128)
    while True:
        client_socket, client_address = server_socket.accept()
        print("用户: %s 接入成功!" % client_address[0])
        handle_client_process = Process(target=handle_client, args=(client_socket, ))
        handle_client_process.start()
        client_socket.close()


