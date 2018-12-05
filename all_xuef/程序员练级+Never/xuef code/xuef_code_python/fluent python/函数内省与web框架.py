
import bobo

@bobo.query('/')
def hello(person):
    return 'Hello %s!' % person

"""
bobo.query 装饰器把一个普通的函数（如 hello）与框架的请求处理
机制集成起来了。装饰器会在第 7 章讨论，这不是这个示例的关键。这
里的关键是，Bobo 会内省 hello 函数，发现它需要一个名为 person
的参数，然后从请求中获取那个名称对应的参数，将其传给 hello 函
数，因此程序员根本不用触碰请求对象。
"""

"""
from clip import clip
>>> from inspect import signature
>>> sig = signature(clip)
>>> sig # doctest: +ELLIPSIS
<inspect.Signature object at 0x...>
>>> str(sig)
'(text, max_len=80)'
>>> for name, param in sig.parameters.items():
... print(param.kind, ':', name, '=', param.default)
...
POSITIONAL_OR_KEYWORD : text = <class 'inspect._empty'>
POSITIONAL_OR_KEYWORD : max_len = 80
"""
