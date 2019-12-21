import threading

def test(g_num):

    for i in range(6):
        g_num += 1
        print(g_num)

g_num = 0


def main():
    # target指定将来这个线程去哪个函数执行代码。
    # args指定将来调用函数的时候传递什么数据过去。
    t1 = threading.Thread(target=test,args=(g_num, ))
    t1.start()


if __name__=='__main__':
    main()
