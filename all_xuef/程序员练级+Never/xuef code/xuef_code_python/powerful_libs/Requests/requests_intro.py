
"""
打开套接字，构建 HTTP 请求，解析响应极其乏味，因此大多数用户使用库来做大部分工作。
"""
import requests
# requests.get 向服务器发送一个 HTTP GET 请求，返回一个包含响应的对象。
response = requests.get('http://aosabook.org/en/500L/web-server/testpage.html')

# 该对象的 status_code 是响应的状态码
print('status code:', response.status_code)

# 它的 content_length 是响应数据的字节数
print('content length:', response.headers['content-length'])
# text 是真正的数据（在这个例子中，是一个 HTML 页面）。
print(response.text)
