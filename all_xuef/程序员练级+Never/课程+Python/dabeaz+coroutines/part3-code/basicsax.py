# basicsax.py
#
# A very simple example illustrating the SAX XML parsing interface

import xml.sax # event-driven xml parser

"""
SAX解析XML速度快、占用内存小。我们只需要关注三个事件：start_element、end_element、char_data。
如：当SAX在解析一个节点时<li><a href="/python">Python</a></li> 会产生三个事件： 
2.1 start_element事件，分别读取<li>、<a href="/python"> 
2.2 end_element事件，分别读取</a>、</li> 
2.3 char_data事件、读取Python
--------------------- 
作者：诺坎普奇迹 
来源：CSDN s
原文：https://blog.csdn.net/wangxingfan316/article/details/77102572

You see this same programming pattern in other settings (e.g., HTMLParser module)
"""
class MyHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.tag_name = ""
        self.ids = []
        
    # 文档启动的时候调用
    def startDocument(self):
        print('XML开始解析...')
        
    def startElement(self,name,attrs):
        self.tag_name = name
        #print ("startElement", name, attrs)
    def endElement(self,name):
        pass
        #print ("endElement", name)
    def characters(self,text):
        if self.tag_name == 'id':
            self.ids.append(text)
            print(text)
        self.tag_name = ""
        #print ("characters", repr(text)[:40])
    # 文档结束的时候调用
    def endDocument(self):
        print('XML文档解析结束!')
        
xml.sax.parse(r"..\coroutines\allroutes.xml",MyHandler())


