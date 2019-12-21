import re


def main():
    url = input('请输入邮箱地址：')
    ret = re.match(r'^[a-zA-Z0-9_-]{4,20}@(163|126|qq)\.com$', url)
    if ret:
        print('正在登陆~~~~')
    else:
        print('请输入正确的网址！xxxx@163.com')


if __name__=='__main__':
    main()
