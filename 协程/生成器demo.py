def fibo(n):
    a = 0
    b = 1
    current = 0
    while n > current:
        yield a  # 如果一个函数中使用了yield，那么这个就不在是一个函数，而是一个生成器模版。
        a, b = b, a+b
        current += 1


obj = fibo(10)
#for i in obj:
#   print(i)
while True:
    try:
        ret = next(obj)  # 启动生成器方式1  第二种使用obj.send()
        print(ret)
    except:
        break
