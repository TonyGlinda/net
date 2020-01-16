import re
contents = """GET /index.html  HTTP/1.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362
Accept-Encoding: gzip, deflate
Host: 127.0.0.1:8080
Connection: Keep-Alive"""

contents_lines = contents.splitlines()
print(contents_lines[0])
rlt = re.search(r'index|(/[^ ]*)', contents_lines[0])
rlt = rlt.group()
print(rlt)
