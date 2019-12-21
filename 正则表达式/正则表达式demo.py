import re

print(re.match('速度与激情[1-8]', '速度与激情1').group())
# [] 匹配[]中列举的字符串，如果匹配，则通过group方法返回，没有则报错。
print(re.match('速度与激情[12345678]', '速度与激情1').group())
# [] 匹配[]中列举的字符串，如果匹配，则通过group方法返回，没有则报错。
print(re.match('速度与激情[a-e]', '速度与激情a').group())
print(re.match('速度与激情[abcde]', '速度与激情b').group())
print(re.match('速度与激情[aA]', '速度与激情A').group())


print(re.match('速度与激情\d', '速度与激情9').group())
# \d匹配数字0-9
print(re.match('速度与激情\d.', '速度与激情10').group())
# .匹配任意一个字符串（除了\n）
print(re.match('速度与激情\D', '速度与激情d').group())
# \D匹配非数字，如果是数字，则报错！


print(re.match('速度与激情\s[0-9]', '速度与激情 1').group(0))
# \s 匹配空白或Tab。 group(args) 参数0代表匹配match所有的正则表达式，1代表第一个
print(re.match('速度与激情\S', '速度与激情1').group())
# \D 匹配非空白或Tab

print(re.match('速度与激情\w', '速度与激情_').group())
# \w匹配所有字符内容，数字、字母、下划线。
print(re.match('速度与激情\W', '速度与激情@').group())
# \W匹配所有非单词字符
