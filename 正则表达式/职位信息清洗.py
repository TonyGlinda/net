import re


def main():
    with open(r'C:\Users\hp-pc\Desktop\test.txt','rb') as file:
        content = file.read().decode('utf-8')
        ret = re.sub(r'<([a-z0-9\s="_-]*>)|<(/[a-z]*\d*)>|\s','',content)
        list_new = re.split(r'；',ret)
        with open(r'C:\Users\hp-pc\Desktop\test2.txt','w+') as new_file:
            for i in list_new:
                new_file.write(i)
                new_file.write('\n')
    print('~~~数据清洗成功~~~~')

if __name__=='__main__':
    main()
