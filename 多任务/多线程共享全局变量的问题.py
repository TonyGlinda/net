import threading
import time


def test1(num):
    global g_num
    for i in range(num):
        g_num += 1
    print(g_num)

def test2(num):
    global g_num
    for i in range(num):
        g_num += 1
    print(g_num)

g_num = 0
def main():
    t1 = threading.Thread(target=test1,args=(1000000,))
    t2 = threading.Thread(target=test2,args=(1000000,))
    # 次数越多，越有可能发生资源竞争的问题。
    t1.start()
    t2.start()
    time.sleep(5)  # 等待5秒，子线程结束。


if __name__ =='__main__':
    main()
