import gevent
from gevent import monkey
import time

monkey.patch_all()  # 将程序中用到的耗时操作的代码，换为gevent中自己实现的模块


def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)


def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)


def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)


gevent.joinall([gevent.spawn(f1,5), gevent.spawn(f2,5),
                gevent.spawn(f3,5)])  # 等待所有协程做完，再结束。
# g1 = gevent.spawn(f1, 5)
# g2 = gevent.spawn(f2, 5)
# g3 = gevent.spawn(f3, 5)
# g1.join()
# g2.join()
# g3.join()




