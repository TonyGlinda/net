import threading
import time


g_num = 0
def test1():
    global g_num
    for i in range(100):
        g_num += 1
    print('work in test1--', g_num)


def test2():
    print('work in test2--', g_num)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    t1.start()
    time.sleep(1)
    t2.start()




if __name__=='__main__':
    main()
