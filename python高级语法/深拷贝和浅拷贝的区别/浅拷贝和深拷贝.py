import copy


a = [4,5,6]

b =[1,2,3]
c = [a,b]
e = copy.copy(c) #浅拷贝，只拷贝了引用，不拷贝内容（指向的数据）
print(id(c[0]))

print(id(e[0])) # c[0]和e[0]的ID相同，说明c,e的内容共同引用了一个数据a
print(id(a))
a.append(6)
print(e)    # e最终指向a,当a发生改变时，e指向的数据内容也会改变。
