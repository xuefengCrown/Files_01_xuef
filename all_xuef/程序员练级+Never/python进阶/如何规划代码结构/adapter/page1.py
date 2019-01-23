import pdb
from render1 import Render, HtmlRender, Adapter_4_HtmlRender
class Page:
    def __init__(self, title, renderer):
        if not isinstance(renderer, Render):
            raise TypeError("Expected obj of type Render, got {}".format(type(render).__name__))
        self.title = title
        self.renderer = renderer
        self.paragraphs = []

    def add_paragraph(self, paragraph):
        self.paragraphs.append(paragraph)

    def render(self):
        self.renderer.header(self.title)
        for p in self.paragraphs:
            self.renderer.paragraph(p)
        self.renderer.footer()

page = Page("适配器", Adapter_4_HtmlRender(HtmlRender()))

page.add_paragraph("适配器模式示例")
page.add_paragraph("-1...")
page.add_paragraph("-2...")
#pdb.set_trace()
page.render()
