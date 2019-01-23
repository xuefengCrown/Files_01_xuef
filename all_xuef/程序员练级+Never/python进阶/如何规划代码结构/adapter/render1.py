
import sys, textwrap

class Render:
    pass
    
class TextRender(Render):
    def __init__(self, width=80, file=sys.stdout):
        self.width = width
        self.file = file
        self.pre = False

    def header(self, title):
        self.file.write("{0:^{2}}\n{1:^{2}\n}".format(title, "="*len(title), self.width))

    def paragraph(self, text):
        if self.pre:
            self.file.write('\n')
        self.file.write(textwrap.fill(text, self.width))
        self.file.write('\n')
        self.pre = True

    def footer(self):
        pass

from html import escape
class HtmlRender: # 不符合Page中定义的渲染器接口
    def __init__(self, file=sys.stdout):
        self.file = file

    def header(self):
        self.file.write("<!doctype html>\n<html>\n")

    def title(self, title):
        self.file.write("<head><title>{}</title></head>\n".format(escape(title)))

    def start_body(self):
        self.file.write("<body>\n")

    def body(self, text):
        self.file.write("<p>{}</p>\n".format(escape(text)))
        
    def end_body(self):
        self.file.write("</body>\n")

    def footer(self):
        self.file.write("</html>\n")


class Adapter_4_HtmlRender(Render): # 适配器
    def __init__(self, htmlRender): # 实际渲染任务都会委托给 htmlRender
        self.htmlRender = htmlRender
        
    def header(self, title):
        self.htmlRender.header()
        self.htmlRender.title(title)
        self.htmlRender.start_body()

    def paragraph(self, text):
        self.htmlRender.body(text)

    def footer(self):
        self.htmlRender.end_body()
        self.htmlRender.footer()



    

















        


























    
























            
