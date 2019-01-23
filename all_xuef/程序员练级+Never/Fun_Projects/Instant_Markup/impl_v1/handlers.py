
class Handler:
    #主要进行方法导航
    def callback(self, prefix, name, *args):
        """根据prefix+name来寻找函数"""
        method = getattr(self, prefix+name, None)
        if callable(method):
            return method(*args)
    def start(self, name):
        self.callback('start_', name)
    def end(self, name):
        self.callback('end_', name)
    def sub(self, name):
        def subit(match): # match 为匹配项
            result = self.callback('sub_', name, match)
            if result is None: match.group(0)
            return result
        return subit


class HTMLRenderer(Handler):
    """
    A specific handler used for rendering HTML.
    The methods in HTMLRenderer are accessed from the superclass
    Handler's start(), end(), and sub() methods. They implement basic
    markup as used in HTML documents.
    """
    def start_document(self):
        print('<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8"/>')
        
    def end_document(self):
        print('</div></body></html>')
        
    def start_paragraph(self):
        print('<p>')
    def end_paragraph(self):
        print('</p>')
        
    def start_heading(self):
        print('<h1>')
    def end_heading(self):
        print('</h1>')

    def start_h2(self):
        print('<h2>')
    def end_h2(self):
        print('</h2>')

    def start_h3(self):
        print('<h3>')
    def end_h3(self):
        print('</h3>')
        
    def start_list(self):
        print('<ul>')
    def end_list(self):
        print('</ul>')
        
    def start_listitem(self):
        print('<li>')
    def end_listitem(self):
        print('</li>')
        
    def start_title(self):
        print('<title>')
    def end_title(self):
        print('</title><link href="./css/style.css" rel="stylesheet" type="text/css"> </head>\
              <div class="container"><body>')

    def start_code(self):
        print('<pre><code>')
    def end_code(self):
        print('</code></pre>')
        
    def sub_emphasis(self, match):
        return '<em>%s</em>' % match.group(1)
    
    def sub_url(self, match):
        link_t = match.group(1)
##        i = link_t.find('/')
##        j = link_t[i+2:].find('/')
##        link_t = link_t[i+2:j]
        return '<a href="%s">%s</a>' % (match.group(1), link_t)
    def sub_mail(self, match):
        return '<a href="mailto:%s">%s</a>' % (match.group(1), match.group(1))
    def feed(self, data):
        print(data)



