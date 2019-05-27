# coding:utf-8
import socket
import re
from multiprocessing import Process
import requests

element = requests.get("https://www.baidu.com")
element.encoding = "utf-8"
element = element.text
print(element)


with open("./baiduhuanchun.html", "wb") as f:
    f.write(element.encode())

# def handle_client(client_socket):
#     print(client_socket)
#     """返回浏览器数据"""
#     while True:
#         request_date = client_socket.recv(1024)
#         if request_date == b"":
#             client_socket.close()
#             print("客户端已断开!")
#             return
#         print(request_date)
#         request = re.sub(r"Host: .*\r\n", "Host: www.baidu.com\r\n", request_date.decode())
#         print(request)
#         server_socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         server_socket1.connect(("www.baidu.com", 80))
#         server_socket1.send(request.encode())
#         while True:
#             server_msg = server_socket1.recv(5000)
#             print(server_msg)
#             if server_msg:
#                 client_socket.send(server_msg)
#             else:
#                 print("信息传送完毕!")
#                 server_socket1.close()
#                 break
#         # client_socket.close()
#
#
# if __name__ == '__main__':
#     # 创建服务器
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
#     ip_port1 = ("", 8000)
#     server_socket.bind(ip_port1)
#     server_socket.listen(128)
#     print("服务已开启!")
#     while True:
#         client_socket, client_address = server_socket.accept()
#         print("用户: %s 接入成功!" % client_address[0])
#         handle_client_process = Process(target=handle_client, args=(client_socket, ))
#         handle_client_process.start()

