import multiprocessing
import os


def download_date(q,q2):
    # 获取目标文件夹内的所有文件名，并加入列表。
    path = r'C:\Users\hp-pc\Desktop\python基础练习题'
    os.chdir(path)
    files_list = os.listdir(path)
    for i in files_list:
        q.put(i)
        with open(i,'rb') as old_f:
            content=old_f.read()
            q2.put(content)
    print('总共复制了%d个文件' % len(files_list))


def copy_date(q,q2):
    path = r'C:\Users\hp-pc\Desktop\test'
    os.makedirs(path)
    os.chdir(path)
    while True:
        file = q.get()  # 从Queue队列获取文件
        # 读取文件内容，把内容重新写入新的文件。
        new_content = q2.get()
        with open(file,'wb') as new_f:
            new_f.write(new_content)
        if q.empty():
            print('文件复制完毕！')
            break


def main():
  # 创建Queue队列，完成文件下载子进程和复制子进程的通信。
    q = multiprocessing.Queue()
    q2 = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=download_date,args=(q,q2))
    p2 = multiprocessing.Process(target=copy_date, args=(q,q2))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
