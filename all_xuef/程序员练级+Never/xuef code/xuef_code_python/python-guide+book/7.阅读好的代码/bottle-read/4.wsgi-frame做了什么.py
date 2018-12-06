
"""
wsgi框架做了什么?
1. app应该是一个可调用对象(函数、类或者是实现了 __call__方法的类的实例)
    class B:
        pass
B()-->返回类实例,B实现了__iter__的话，B()就是可迭代的。

2. 这个可调用对象应该遵守协议(接收 environ, start_response 两个参数)

3. 该可调用对象必须返回一个可迭代对象(Response Body)

"""

# 解析 query_string
## from urllib.parse import parse_qs

# environ的解析
## webob
## 多值字典
from webob.multidict import MultiDict


"""
广义地说，Web框架包含一系列库和一个主要的处理器（handler），这样您就能够构建自己的代码来
实现Web应用 （比如说一个交互式的网站）。大多数web框架包含模式和工具，至少实现以下功能：

URL路由（URL Routing）
    将输入的HTTP请求匹配到特定的Python代码用来调用
    
请求和响应对象（Request and Response Objects）
    封装来自或发送给用户浏览器的信息
    
模板引擎（Template Engine）
    能够将实现应用的Python代码逻辑和其要产生输出的HTML（或其他）分离开
    
Web服务器开发（Development Web Server）
    在开发机上运行HTTP服务器，从而快速开发；当文件更新时自动更新服务端代码。
"""
