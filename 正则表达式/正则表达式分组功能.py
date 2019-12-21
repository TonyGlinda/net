import re

# | 匹配任意一个正则表达式，（ab）将括号内的作为一个分组
ret = re.match(r'(速度与激情)([0-9])|([a-zA-Z])','速度与激情8')
print(ret.group(0))  # 0代表获取所有分组的值，1代表第一个分组，一次类推。

# \num 引用分组内匹配到的字符串
html_str = '<h1>hahaha</h1>'
ret = re.match(r'<(\w*)>\w*<(/\1)>', html_str)
print(ret.group())

# 分组起别名(?P<name>)   引用分组别名name匹配到的字符串(?P=name)
ret = re.match(r'<(?P<p1>\w*)>\w*<(/(?P=p1))>', html_str)
print(ret.group())
