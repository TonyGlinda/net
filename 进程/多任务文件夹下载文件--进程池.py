import os
import multiprocessing


def copy_file(old_file_names,path,path_copy,new_file_name):
    flag = 0
    for file in old_file_names:
        os.chdir(path)
        with open(file,'rb') as old_f:
            content = old_f.read()
            os.chdir(path_copy)
            with open(new_file_name,'wb') as new_f:
                new_f.write(content)
                flag += 1
                print('\r已经复制了%.2f%%'%(flag*100/len(old_file_names)),end='')


def main():
    path = input('请输入要copy的文件夹的路径：')
    #path = r'C:\Users\hp-pc\Desktop\python基础练习题'
    old_file_names = os.listdir(path)   # 获取文件夹内的文件名字
    path_copy = r'C:\Users\hp-pc\Desktop\test2'
    os.makedirs(path_copy)  # 建立一个新的文件夹

    po = multiprocessing.Pool(5)  # 创建进程池，实现自动创建子进程，完成多任务。
    for new_file_name in old_file_names:
        po.apply_async(copy_file, args=(old_file_names,path,path_copy,new_file_name))
    po.close()
    po.join()


if __name__ == '__main__':
    main()

