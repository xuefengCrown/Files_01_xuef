
"""

如果我们直接将 bottle.py 下载到自己的应用中的话，我们可以建立下面这样的目录结构：
    + application
    +----bottle.py
    +----app.py
我们可以将下面的创建 Bottle 实例的示例代码复制到 app.py 文件中，运行该文件即可。

"""

"""
from bottle import Bottle, run
app = Bottle()
@app.route('/hello')
def hello():
    return "Hello World!"
run(app, host='localhost', port=8080)

    #Bottle server starting up (using WSGIRefServer())...
    #Listening on http://localhost:8080/
    #Use Ctrl-C to quit.
"""
