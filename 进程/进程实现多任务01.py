import multiprocessing,time


def test1():
    for i in range(4):
        print('~~~~~test1~~~~', i)
        time.sleep(1)


def test2():
    for i in range(4):
        print('~~~test~~~~', i)
        time.sleep(1)


def main():
    p1 = multiprocessing.Process(target=test1)
    p2 = multiprocessing.Process(target=test2)
    p1.start()
    p2.start()


if __name__=='__main__':
    main()


