
"""
Recursive Objects
Objects can have other objects as attribute values.
When an object of some class has an attribute value of that same class,
it is a recursive object.
"""

class Link:
    """A linked list with a first element and the rest."""
    empty = ()
    def __init__(self, first, rest = empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i==0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)

def link_expression(s):
    """Return a string that would evaluate to s."""
    if s.rest is Link.empty:
        rest = ''
    else:
        rest = ', ' + link_expression(s.rest)
    return 'Link({0}{1})'.format(s.first, rest)

def extend_link(s, t):
    """builds a linked list containing the elements of one Link instance s followed
        by the elements of another Link instance t.
    """
    if s is Link.empty:
        return t
    else:
        # 此处要使用Link重新构造链表
        return Link(s.first, extend_link(s.rest, t))
p=print
## test Link    
s = Link(3, Link(4, Link(5)))
p(len(s))
p(s[2])
## __repr__
Link.__repr__ = link_expression
##p(Link.__dict__)
p(s)


# 闭包性质
#The Link class has the closure property. Just as an element of a list can
#itself be a list, a Link can contain a Link as its first element.
s_first = Link(s, Link(6))
p(s_first)

# Recursive functions are particularly well-suited to manipulate linked lists.


## __add__
Link.__add__ = extend_link
p(s + s)

## map, 构造函数+选择函数来实现
def map_link(f, s):
    """
    The map_link function defined below applies a function f to each element of a
    linked list s and constructs a linked list containing the results.
    """
    if s is Link.empty:
        return Link.empty
    else:
        return Link(f(s.first), map_link(f, s.rest))

ret = map_link(lambda i: i*i, s)
p(ret)

## filter
##The filter_link function returns a linked list containing all elements of a
##linked list s for which f returns a true value. The combination of map_link and
##filter_link can express the same logic as a list comprehension.
def filter_link(f, s):
    # 代码是简单的，因为filter背后的逻辑很简单，就是个二分
    if s is Link.empty:
        return Link.empty
    flag = f(s.first)
    if flag is True:
        return Link(s.first, filter_link(f, s.rest))
    else:
        return filter_link(f, s.rest)

odd = lambda x: x%2 == 1
##p(is_odd(3))
p(filter_link(odd, s))

square = lambda x: x*x
r1 = map_link(square, filter_link(odd, s)) #Link(9, Link(25))
p(r1)
p([square(x) for x in [3, 4, 5] if odd(x)])
