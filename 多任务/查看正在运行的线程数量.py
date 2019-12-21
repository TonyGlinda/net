import threading
import time

def dance():
    for i in range(5):
        print('~~~~~~dance~~~~~~', i)
        time.sleep(1)


def sing():
    for i in range(8):
        print('~~~~~~~sing~~~~~~~', i)
        time.sleep(1)


def main():
    # 在调用threading之前查看线程数量
    print(threading.enumerate())
    t1 = threading.Thread(target=dance)
    t2 = threading.Thread(target=sing)
    # 在创建对象后查看线程数量
    print(threading.enumerate())
    t1.start()  # 一个线程的执行是以start（）调用开始的。
    time.sleep(1)
    t2.start()
    # 在调用start()后查看线程数量
    print(threading.enumerate())



if __name__ =='__main__':
    main()
