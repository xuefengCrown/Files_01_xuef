
模块
1）启动模块
2）连接器模块
3）核心模块

1）启动模块
BootStrap
2）连接器模块
The connector and its supporting class (HttpConnector and HttpProcessor).
	HttpConnector: 等待 HTTP 请求
	HttpProcessor: 创建 Request对象和 Response 对象
	
The class representing HTTP requests (HttpRequest) and its supporting classes.
	HttpRequest: 
		要设置的值包括: URI, query string, parameters, cookies and other headers, etc. 

The class representing HTTP responses (HttpResponse) and its supporting classes.
Façade classes (HttpRequestFacade and HttpResponseFacade).
The Constant class.

3）核心模块
ServletProcessor and StaticResourceProcessor.


解析 HTTP 请求
1）读取套接字的输入流
2）解析请求行
3）解析请求头
4）解析Cookie
5）获取参数
?k1=v1&k2=v2
查询字符串可能包含一个会话标识符 jsessionid
参数可能出现在查询字符串或请求头中