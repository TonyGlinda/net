from _collections_abc import Iterable


class My_test(object):
    def __init__(self):
        self.names = list()

    def add_name(self,name):
        self.names.append(name)


    def __iter__(self):
        '''如果一个对象称为一个 可迭代对象，即可以使用for，那么必须实现__iter__方法'''
        return ClassIterator(self)

class ClassIterator(object):
    def __init__(self,obj):
        self.obj=obj
        self.current = 0
    def __iter__(self):
        pass
    def __next__(self):
        ret=self.obj.names[self.current]
        self.current += 1
        return ret


my = My_test()
my.add_name('tony')
my.add_name('Glinda')
my.add_name('Tom')
#print(isinstance(my,Iterable))
for name in my:
    print(name)
