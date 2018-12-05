
import http.server # https://docs.python.org/3/library/http.server.html
import os
import pdb
from urllib.parse import unquote

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            #print(self.headers)
            # 这里假设允许程序使用所在路径（就是使用 os.getcwd 所得到的）下的任意文件提供服务。
            fname = self.path[1:]
            full_path = os.path.join(os.getcwd(), unquote(fname,'utf-8'))
            #pdb.set_trace()
            # 文件不存在
            if not os.path.exists(full_path):
                raise ServerException("'{0}' not found".format(self.path))
            elif os.path.isfile(full_path):
                self.handle_file(full_path)
            # ... it's sth we don't handle
            else:
                raise ServerException("Unknown object '{0}'".format(self.path))
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
    
