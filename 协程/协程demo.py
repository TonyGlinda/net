import time


def test1():
    while True:
        print('~~~~test1~~~~')
        time.sleep(0.1)
        yield


def test2():
    while True:
        print('~~~~test2~~~~')
        time.sleep(0.1)
        yield


def main():
    t1 = test1()
    t2 = test2()
    while True:
        next(t1)
        next(t2)


if __name__ == '__main__':
    main()
