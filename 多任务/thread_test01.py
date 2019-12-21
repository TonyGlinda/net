import threading
import time

def dance():
    for i in range(5):
        print('~~~~dance~~~', i)
        time.sleep(1)

def sing():
    for i in range(5):
        print('~~~sing~~~', i)
        time.sleep(1)


t1 = threading.Thread(target=dance)
t2 = threading.Thread(target=sing)
t1.start()       # 一个线程的运行是以start()的调用开始。
t2.start()

