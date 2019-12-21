import multiprocessing
# put()放入数据 get()获取数据，没有了就阻塞 get_nowait()获取数据，没有了报错。
# q.full()检查数据是否放满，q.empty()检查队列是否为空。

def download_file(q):
    date = [11,'22',1212]
    for i in date:
        q.put(i)   # 将数据放入Queue队列


def analysis_date(q):
    date_list = list()
    while True:
        date = q.get()    # 不断从Queue队列中获取数据，直到队列为空。
        date_list.append(date)
        if q.empty():
            break
    print(date_list)


def main():
    q = multiprocessing.Queue()  # 创建一个Queue队列
    p1 = multiprocessing.Process(target=download_file,args=(q,))
    p2 = multiprocessing.Process(target=analysis_date,args=(q,))
    p1.start()
    p2.start()

if __name__=='__main__':
    main()
