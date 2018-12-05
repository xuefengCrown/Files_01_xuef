import http.server
class RequestHandler(http.server.BaseHTTPRequestHandler):
    '''Handle HTTP requests by returning a fixed 'page'.'''
    # Page to send back.
    Page = '''\
        <html>
        <body>
        <p>Hello, web!</p>
        </body>
        </html>
        '''
    # Handle a GET request.
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(self.Page)))
        self.end_headers()# 插入空行以分隔首部和页面本身
        self.wfile.write(self.Page.encode())
#----------------------------------------------------------------------
if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = http.server.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
    
