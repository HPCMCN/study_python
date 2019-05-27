import threading
a = 1


def fun1():
    for i in range(1000000):
        global a
        a += 1
        print(a)


if __name__ == '__main__':
    t1 = threading.Thread(target=fun1)
    t2 = threading.Thread(target=fun1)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(a)
