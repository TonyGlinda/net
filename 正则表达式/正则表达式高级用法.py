import re

# 替换字符串中的某些字符串
ret = re.sub(r'\d{4}','2020', '今年是2019年！2019年')
print(ret)

# 搜索字符串中的符合正则表达式的字符串,但是只能找一个
ret =re.search(r'\d+','今年是2019年！2019年')
print(ret.group())

# 将字符串按照正则表达式切片，返回一个列表
ret = re.split(r'！','今年是2019年！2019年')
print(ret)

# 寻找字符串中符合正则表达式的字符串，并返回一个列表！可以找多个！
ret = re.findall(r'\d{4}', '今年是2019年！2019年')
print(ret)
