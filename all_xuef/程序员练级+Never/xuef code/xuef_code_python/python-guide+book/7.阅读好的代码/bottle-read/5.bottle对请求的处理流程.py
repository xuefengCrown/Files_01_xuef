
"""
1. wsgi 启动，加载 bottle 应用，监听在设置的端口(?)

2. 请求进来之后，被 wsgi server 封装好，调用 Bottle 的 __call__ 函数，交给 bottle 处理

3. bottle 根据传过来的 environ 字典，初始化 request 和 response 对象

4. bottle 获取传过来的 url 值，匹配之前根据代码中装饰器生成的路由器对象，找到处理函数

5. 调用处理函数

6. 处理函数会使用默认的模板引擎，替换所有的变量，返回处理结果

7. 把处理函数返回的值封装成 wsgi 兼容的对象

8. 把封装好的 response 返回给 wsgi server


"""
