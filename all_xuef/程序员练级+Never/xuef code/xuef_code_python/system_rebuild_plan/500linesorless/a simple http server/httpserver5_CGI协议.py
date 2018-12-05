"""
大多数人不想为了添加新的功能而编辑 web 服务器的源代码。
为了将他们从编辑源码拯救出来，服务器一般都支持一种叫做公共网关接口（CGI）的机制，
它为 web 服务器提供了一个标准的方式来运行外部程序，以响应请求。

为了让 web 服务器运行这个程序，我们添加了下面的事件处理器：
class case_cgi_file(object):
"""
import http.server # https://docs.python.org/3/library/http.server.html
import os
import pdb
from urllib.parse import unquote

class case_no_file(object):
    '''File or directory does not exist.'''
    def test(self, handler):
        return not os.path.exists(handler.full_path)
    def act(self, handler):
        raise ServerException("'{0}' not found".format(handler.path))
class case_existing_file(object):
    '''File exists.'''
    def test(self, handler):
        return os.path.isfile(handler.full_path) and \
               not handler.full_path.endswith('.py')
    def act(self, handler):
        handler.handle_file(handler.full_path)

class case_directory_index_file(object):
    '''Serve index.html page for a directory.'''
    def index_path(self, handler):
        return os.path.join(handler.full_path, 'index.html')
    def test(self, handler):
        return os.path.isdir(handler.full_path) or \
               os.path.isfile(self.index_path(handler))
    def act(self, handler):
        handler.list_dir(handler.full_path)

# 支持运行 .py 程序 
class case_cgi_file(object):
    '''Something runnable.'''
    def test(self, handler):
        return os.path.isfile(handler.full_path) and \
               handler.full_path.endswith('.py')
    def act(self, handler):
        handler.run_cgi(handler.full_path)
        
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
    ##完整的 CGI 协议比这更丰富，它允许 URL 中存在参数，服务器会将它们传入正在运行的程序，
    ##但这些细节并不会影响系统的整体架构
    
    def run_cgi(self, full_path):
        cmd = "C:\Python36\python " + "\""+ full_path + "\""
        pipe = os.popen(cmd, 'r')
        pdb.set_trace()
        data = pipe.read()
        pipe.close()
        self.send_content(data.encode())
        
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
    def list_dir(self, full_path):
        try:
            entries = os.listdir(full_path)
            bullets = ['<li>{0}</li>'.format(e)
                for e in entries if not e.startswith('.')]
            page = self.Listing_Page.format('\n'.join(bullets))
            self.send_content(page.encode())
        except OSError as msg:
            msg = "'{0}' cannot be listed: {1}".format(self.path, msg)
            self.handle_error(msg)
            
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
        
    def handle_file(self, full_path):
        try:
            # 在使用文件提供服务时，将整个文件读入内存在真实生活中并不合适，
            # 视频文件大小可能是好几G。处理上述情况已经超出了本章的范围。
            with open(full_path, 'rb') as reader:
                content = reader.read()
            self.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(self.path, msg)
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
    serverAddress = ('', 8080)
    server = http.server.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
    
