from gevent import monkey
import gevent
import urllib.request


monkey.patch_all()
def download_msg():
    link_address = r"http://c.hiphotos.baidu.com/video/pic/item/8435e5dde71190efff115430c01b9d16fcfa6073.gif"
    ret = urllib.request.urlopen(link_address)
    content = ret.read()
    with open('01', 'wb') as f:
        f.write(content)
def main():
    gevent.joinall([gevent.spawn(download_msg)])


if __name__=='__main__':
    main()
