
"""
生成 html 元素
"""
import html

"""
name: 标签名,如<a></a>-->name: a
value: 文本
"""
def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)

    ele = "<{name} {attrs}>{value}</{name}>".format(
        name = name,
        value = html.escape(value),
        attrs = attr_str)
    return ele

import os
def genHTM():
    path = os.getcwd()
    # C:\\code_dxf\\xuefgit\\Files_01_xuef\\all_xuef\\程序员练级+Never\\
    txtname = path + "\\pythonBooks.txt"
    htmname = path + "\\pythonBooks.htm"
    f_txt = open(txtname, encoding='utf-8')
    f_htm = open(htmname, 'w', encoding='utf-8')
    for line in f_txt:
        if line is not None:
            value, url = line.rstrip('\n').split(';')
            alink = make_element('a', value,
                        target = '_blank',
                        href = url) + '<br>'
            print(alink)
            f_htm.write(alink)

    f_txt.close()
    f_htm.close()

