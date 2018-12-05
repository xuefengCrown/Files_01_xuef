
"""
假设我们在开发一个调试 Web 应用的工具，我们想生成 HTML，显示不
同类型的 Python 对象。
"""

import html

def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)
