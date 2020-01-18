# WSGI协议介绍。
## WSGI
怎么在你刚建立的web服务器上运行一个Django应用和Flask应用，如何
不做任何改变而适应不同的web架构呢？
## WSGI协议的定义。
WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求。
我们来看一个简单的web版本的‘Hello World’:
 def application(environ, start_response)"
     start_response('200 ok',[('content-Type', 'text/html')])
     return 'Hello World！'
上面的application()函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：
- environ:一个包含所有HTTP请求信息的dict对象；
- start_response:一个发送HTTP响应的函数。
整个application()函数本身没有涉及到任何解析HTTP的部分，也就是说，把底层web
服务器和应用程序逻辑部分进行了分离，这样开发者就可以专心做一个领域了。

application()函数必须由WSGI服务器来调用。有很多符合WSGI规范的服务器，而我们此时
的web服务器项目的目的就是做一个技能解析静态网页还可以解析动态网页的服务器。
