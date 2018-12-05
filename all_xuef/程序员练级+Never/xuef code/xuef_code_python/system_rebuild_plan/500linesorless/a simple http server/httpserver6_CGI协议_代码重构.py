"""
原生的代码和重构后版本的差异反映了两个很重要的观念。
第一个是把类看作是相关服务的一个集合。RequestHandler 和 base_case 并不作出决定或采取行动；
它们只为其他做这些事的类提供工具。

第二个是可拓展性: 人们可以通过写一个外部的 CGI 程序，或者增加一个事件处理类，来为我们的
web 服务器增加新的功能。后者需要在 RequestHandler 中改变一行（将事件处理器插入事件列表），
但我们可以让 web 服务器读一个配置文件，并从中加载事件处理类来摆脱上述改变。

在这两种情况下，他们可以忽略大部分低层次细节，正如 BaseHTTPRequestHandler 类的开发者允许
我们忽略处理套接字连接的细节和解析 HTTP 请求。

这些观念通常很有用；试试看你能否找到方法，将他们应用到你自己的项目中。
"""
import http.server # https://docs.python.org/3/library/http.server.html
import os
import pdb
from urllib.parse import unquote

class base_case(object):
    def test(self,handler):
        pass
    def act(self, handler):
        pass
    
class case_no_file(base_case):
    '''File or directory does not exist.'''
    def test(self, handler):
        return not os.path.exists(handler.full_path)
    def act(self, handler):
        raise ServerException("'{0}' not found".format(handler.path))
class case_existing_file(base_case):
    '''File exists.'''
    def test(self, req_handler):
        return os.path.isfile(req_handler.full_path) and \
               not req_handler.full_path.endswith('.py')
    def act(self, req_handler):
        self.handle_file(req_handler)
    ##??? handle_file 应该存在哪个类中???
    def handle_file(self, req_handler):
        try:
            # 在使用文件提供服务时，将整个文件读入内存在真实生活中并不合适，
            # 视频文件大小可能是好几G。处理上述情况已经超出了本章的范围。
            with open(req_handler.full_path, 'rb') as reader:
                content = reader.read()
            req_handler.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(req_handler.path, msg)
            req_handler.handle_error(msg)

class case_directory_index_file(base_case):
    '''Serve index.html page for a directory.'''
    # How to display a directory listing.
    Listing_Page = '''\
        <html>
        <body>
        <ul>
        {0}
        </ul>
        </body>
        </html>
        '''
    def index_path(self, handler):
        return os.path.join(handler.full_path, 'index.html')
    def test(self, req_handler):
        return os.path.isdir(req_handler.full_path) or \
               os.path.isfile(self.index_path(req_handler))
    def act(self, req_handler):
        self.list_dir(req_handler)
    def list_dir(self, req_handler):
        try:
            entries = os.listdir(req_handler.full_path)
            bullets = ['<li>{0}</li>'.format(e)
                for e in entries if not e.startswith('.')]
            page = self.Listing_Page.format('\n'.join(bullets))
            req_handler.send_content(page.encode())
        except OSError as msg:
            msg = "'{0}' cannot be listed: {1}".format(req_handler.path, msg)
            req_handler.handle_error(msg)
# 支持运行 .py 程序 
class case_cgi_file(base_case):
    '''Something runnable.'''
    def test(self, req_handler):
        return os.path.isfile(req_handler.full_path) and \
               req_handler.full_path.endswith('.py')
    def act(self, req_handler):
        self.run_cgi(req_handler)
        
    ##完整的 CGI 协议比这更丰富，它允许 URL 中存在参数，服务器会将它们传入正在运行的程序，
    ##但这些细节并不会影响系统的整体架构
    ## ?安全问题如何保证!!
    def run_cgi(self, req_handler):
        cmd = "C:\Python36\python " + "\""+ req_handler.full_path + "\""
        pipe = os.popen(cmd, 'r')
        data = pipe.read()
        pipe.close()
        req_handler.send_content(data.encode())
class case_always_fail(object):
    '''Base case if nothing else worked.'''
    def test(self, handler):
        return True
    def act(self, handler):
        raise ServerException("Unknown object '{0}'".format(handler.path))

    
class RequestHandler(http.server.BaseHTTPRequestHandler):
    """
    If the requested path maps to a file, that file is served.
    If anything goes wrong, an error page is constructed.
    """
    Cases = [case_no_file(),
             case_existing_file(),
             case_directory_index_file(),
             case_cgi_file(),
             case_always_fail()]
            
    def do_GET(self):
        try:
            #print(self.headers)
            # 这里假设允许程序使用所在路径（就是使用 os.getcwd 所得到的）下的任意文件提供服务。
            fname = self.path[1:]
            full_path = os.path.join(os.getcwd(), unquote(fname,'utf-8'))
            self.full_path = full_path.rstrip("\\")
            #pdb.set_trace()
            # Figure out how to handle it.
            for case in self.Cases:
                if case.test(self):
                    case.act(self)
                    break
        # Handle errors.
        except Exception as msg:
            self.handle_error(msg)
            
    Error_Page = """\
        <html>
        <body>
        <h1>Error accessing {path}</h1>
        <p>{msg}</p>
        </body>
        </html>
        """
    # Handle unknown objects.
    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content, 404)
    # Send actual content.
    def send_content(self, content, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/plain;charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

#----------------------------------------------------------------------
if __name__ == '__main__':
    serverAddress = ('', 80)
    server = http.server.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
    
