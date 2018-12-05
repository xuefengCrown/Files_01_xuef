
# （http://docs.python-requests.org)
import requests

## 提取HEAD数据
url = 'http://python.jobbole.com/81820/?utm_source=blog.jobbole.com&utm_medium=relatedPosts'
resp = requests.head(url)

status = resp.status_code
##last_modified = resp.headers['last-modified']
##content_type = resp.headers['content-type']
##content_length = resp.headers['content-length']

print(resp)

## 下面是一个利用requests通过基本认证登录Pypi的例子：

resp = requests.get('http://pypi.python.org/pypi?:action=login',
                    auth=('user','password'))


##下面是一个利用requests将HTTP cookies从一个请求传递到另一个的例子：

# First request
url="https://music.163.com/#/song?id=28557036"
resp1 = requests.get(url)

# Second requests with cookies received on first requests
##resp2 = requests.get(url, cookies=resp1.cookies)


# 最后但并非最不重要的一个例子是用requests上传内容：
url = 'http://httpbin.org/post'
files = { 'file': ('data.csv', open('data.csv', 'rb')) }

r = requests.post(url, files=files)


## 同样地，如果必须编写涉及代理、认证、cookies以及其他一些细节方面的代码，
## 那么使用 urllib 就显得特别别扭和啰嗦。




