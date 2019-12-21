class Feibo():
    '''用迭代器完成斐波那契数列 0,1,1,2,3,5,8...'''
    def __init__(self,n):
        self.n = n
        self.a = 0
        self.b = 1
        self.current = 0


    def __iter__(self):
        return self


    def __next__(self):
        if self.current <= self.n:
            ret = self.a
            self.a,self.b = self.b,self.a+self.b
            self.current += 1
            return ret
        else:
            raise StopIteration  # 超出范围抛出异常，自动停止。


fibo = Feibo(10)
for num in fibo:
    print(num)
