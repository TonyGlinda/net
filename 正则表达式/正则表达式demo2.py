import re


print(re.match(r'\d{4}-\d{7}', '0838-6705889').group())
# {m} 匹配前一个正则表达式出现m次。
print(re.match(r'\d{3,4}-\d{7,11}', '028-85938399').group())
# ｛m,n｝匹配前一个正则表达式出现从m到n次。 注意逗号后不能有空格！！
print(re.match(r'\d{3,4}-?\d{7,11}', '02885938399').group())
# ？匹配前一个字符串出现一次或者0次。
print(re.match(r'\d{3,4}-*\d{7,11}', '028--85938399').group())
# *匹配前一个字符串出现多次或者无限次。可有可无
print(re.match(r'\d{3,4}-+\d{7,11}', '028-85938399').group())
# +匹配前一个字符串出现1次或者无限次。至少一次。
