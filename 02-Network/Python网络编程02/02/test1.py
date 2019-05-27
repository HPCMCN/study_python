# 需求: 在同一时间完成多个任务.(唱歌和跳舞)
#   办法: 多线程！
import threading
import time


def sing(num):
    print(threading.current_thread())
    for i in range(num):
        print('唱歌...', i+1)
        # 添加延时操作，能够看到多任务同时执行
        time.sleep(0.1)


def dance(name, age, address):
    print(threading.current_thread())
    print(name, age, address)


if __name__ == '__main__':
    # 创建两个线程，分别执行唱歌和跳舞(实现多任务)
    t1 = threading.Thread(target=sing, name='sing', args=(3, ))
    t2 = threading.Thread(target=dance, name='dance', kwargs={'name': '张三','age': 18,'address': '北京三里屯！！！'})

    t1.start()
    t2.start()

    print('主程序执行完毕！')
