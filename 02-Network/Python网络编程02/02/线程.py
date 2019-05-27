import threading as t
import time


def test():
    print("------test%d------")
    time.sleep(1)


for i in range(5):
    test1 = t.Thread(target=test)
    test1.start()
