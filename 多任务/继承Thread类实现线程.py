import threading

class MyThread(threading.Thread):
    # 通过类实现线程主要运用在比较复杂的程序内
    def run(self):
        self.login()
        for i in range(6):
            msg = 'I\'m ' + self.name + str(i)
            print(msg)
        self.register()


    def login(self):
        print('这是登陆……')


    def register(self):
        print('这是注销……')

def main():
    t1 = MyThread()
    t1.start()  # t1.login() 这是调用类的方法，不是多任务！

if __name__=='__main__':
    main()
