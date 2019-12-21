import threading


def test1(num):
    global g_num
    mutex.acquire()  # 上锁，如果之前没有被上锁，那么此时上锁成功，如果已经被上锁，此时堵塞。
    for i in range(num):
        g_num += 1
    mutex.release()  # 解锁
    print(g_num)


def test2(num):
    global g_num
    mutex.acquire()
    for i in range(num):
        g_num += 1
    mutex.release()
    print(g_num)


g_num = 0
# 创建互斥锁
mutex = threading.Lock()
def main():
    t1 = threading.Thread(target=test1,args=(1000000,))
    t2 = threading.Thread(target=test2,args=(1000000,))
    t1.start()
    t2.start()

if __name__ =='__main__':
    main()
