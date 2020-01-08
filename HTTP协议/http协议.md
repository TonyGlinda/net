# HTTP协议
# Http协议简介
- 在web应用中，服务器把网页传给浏览器，实际上就是把网页的HTML代码发送给浏览器，让
浏览器显示出来。而浏览器和服务器之间的传输协议是HTTP，所以：
  - HTML是一种用来定义网页的文本，会HTML，就可以编写网页；
  - HTML是在网络上传输HTML的协议，用于浏览器和服务器的通信。
  
  - 格式
  - 浏览器------->服务器发送请求的格式
    GET / HTTP/1.1
    Host: 192.168.235.1:8080
    Connection: keep-alive
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
    Accept-Encoding: gzip, deflate
    Accept-Language: zh-CN,zh;q=0.9


  -服务器-------->浏览器回送的数据格式如下：
    HTTP/1.1 200 OK
    Bdpagetype: 2
    Bdqid: 0xef29a31400007eb7
    Cache-Control: private
    Connection: keep-alive
    Content-Encoding: gzip
    Content-Type: text/html;charset=utf-8
    Date: Wed, 18 Dec 2019 12:08:05 GMT
    Expires: Wed, 18 Dec 2019 12:08:05 GMT
    Server: BWS/1.1
    Set-Cookie: BDSVRTM=367; path=/
    Set-Cookie: BD_HOME=1; path=/
    Set-Cookie: H_PS_PSSID=1427_21115_30210_30284_26350; path=/; domain=.baidu.com
    Strict-Transport-Security: max-age=172800
    Traceid: 1576670885023818701817233484755404619447
    X-Ua-Compatible: IE=Edge,chrome=1
    Transfer-Encoding: chunked
