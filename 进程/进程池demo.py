from multiprocessing import Pool
import time,os,random


def work(i):
    t_start = time.time()
    print('进程%s 进程号是%d' % (i, os.getpid()))
    time.sleep(random.random()*2)
    t_end = time.time()
    print('进程%s总共花费了%.3f秒' % (i,t_end-t_start))


def main():
    po = Pool(3)  # 建立进程池。
    for i in range(0,10):
        po.apply_async(work,(i,))   # 子进程调用目标。
    print('~~~~start~~~')
    po.close()  # 关闭进程池
    po.join()  # 等待po中所有子进程结束，必须放在close之后。
    print('~~~~end~~~~~')


if __name__ =='__main__':
    main()
