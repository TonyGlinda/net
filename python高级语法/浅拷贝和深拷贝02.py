import copy


a = [4,5,6]
b =[1,2,3]
c = [a,b]
e = copy.deepcopy(c) #深拷贝，单独开辟一个地址，对象的全部进行拷贝！
print(id(c[0]))
print(id(e[0])) # c[0]和e[0]的ID不相同，说明c,e的内容没有引用了一个数据a
a.append(33)
print(c)
print(e)  # 当a发生改变时，深拷贝e时，把数据也进行了拷贝，单独开辟了空间，指向另外的地址！
print(id(e))
