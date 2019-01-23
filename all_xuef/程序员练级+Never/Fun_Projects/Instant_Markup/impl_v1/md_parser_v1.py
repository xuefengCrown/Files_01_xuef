

import sys, re
from handlers import *
from util import *
from rules import *

class Parser:
    """
    A Parser reads a text file, applying rules and controlling a
    handler.
    """
    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []
    def addRule(self, rule):
        self.rules.append(rule)

    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        self.handler.start('document')
        for block in blocks(file): # 每个块都要流过逐个过滤器和规则处理器
            for filter in self.filters:
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last: break
        self.handler.end('document')


class BasicTextParser(Parser):
    """
    A specific Parser that adds rules and filters in its
    constructor.
    """
    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(H3Rule())
        self.addRule(H2Rule())
        self.addRule(HeadingRule())
        self.addRule(CodeRule())
        self.addRule(ParagraphRule())
        self.addFilter(r'\*\*(.+?)\*\*', 'emphasis')
        self.addFilter(r'((http|https)://[\.a-zA-Z0-9-_/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')

        
handler = HTMLRenderer()
parser = BasicTextParser(handler)
import os.path

with open("all_contents.txt", "rt", encoding="utf-8") as sf:
    for line in sf:
        txt_file, html_file, title = line.split(';')
        with open(os.path.join("notes",html_file.strip()), "wt", encoding="utf-8") as o:
            sys.stdout = o
            with open(os.path.join("notes",txt_file.strip()), "rt", encoding="utf-8") as f:
                parser.parse(f)





                
