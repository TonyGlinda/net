import pymysql


def main():
    # 创建connection连接
    conn = pymysql.connect(host='localhost',port=3306,database='goods_test',
                           user='root',password='xc121538',charset='utf8')
    # 获得游标cursor对象
    cls = conn.cursor()
    #
    count = cls.execute('select name from goods where id>10;')
    print('一共获得%d条数据' % count)
    for i in range(count):
        rlt = cls.fetchall()
        for temp in rlt:
            print(temp)

if __name__=='__main__':
    main()
