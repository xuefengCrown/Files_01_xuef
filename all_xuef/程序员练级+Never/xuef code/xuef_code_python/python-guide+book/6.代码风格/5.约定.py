
#这里有一些您应该遵循的约定，以让您的代码更加易读。

##检查变量是否等于常量
##您不需要明确地比较一个值是True，或者None，或者0 - 您可以仅仅把它放在if语句中。
##参阅 真值测试 来了解什么被认为是false。

##糟糕:
if attr == True:
    print 'True!'

if attr == None:
    print 'attr is None!'

##优雅:

# 检查值
if attr:
    print 'attr is truthy!'

# 或者做相反的检查
if not attr:
    print 'attr is falsey!'

# or, since None is considered false, explicitly check for it
if attr is None:
    print 'attr is None!'

## 2.访问字典元素

##不要使用 dict.has_key() 方法。取而代之，使用 x in d 语法，或者 将一个默认参数传递给 dict.get()。

##糟糕:
d = {'hello': 'world'}
if d.has_key('hello'):
    print d['hello']    # 打印 'world'
else:
    print 'default_value'

##优雅:
d = {'hello': 'world'}

print d.get('hello', 'default_value') # 打印 'world'
print d.get('thingy', 'default_value') # 打印 'default_value'

# Or:
if 'hello' in d:
    print d['hello']

## 3.维护列表的捷径
##列表推导 提供了一个强大的而又简洁的方式来处理列表。而且， map() 和 filter()
##函数使用一种不同但是更简洁的语法处理列表。

##过滤列表

##糟糕:
##在迭代列表的过程中，永远不要从列表中移除元素。

# 过滤大于 4 的元素
a = [3, 4, 5]
for i in a:
    if i > 4:
        a.remove(i)
##不要在列表中多次遍历。

while i in a:
    a.remove(i)

##优雅:
##Python有一些标准的过滤列表的方法。 您要使用哪种方法取决于：
##Python 2.x vs. 3.x
##列表 vs. 迭代器
##修改原始列表可能产生的副作用
##Python 2.x vs. 3.x
##从 Python 3.0 开始， filter() 函数返回迭代器而不是列表。
##如果你真的需要一个列表，请使用 list() 将其包装。

##list(filter(...))
##列表推导和生成器表达式在 2.x 和 3.x 中的工作方式相同
##（唯一特殊的是在 2.x 中变量“泄漏”到了闭包空间中）
##
##* 推导会创建一个新的列表对象
##* 生成器会迭代原始列表
##
##filter() 函数
##
##* 在 2.x 中返回一个列表（如果你想要一个迭代器，请使用 itertools.ifilter）
##* 在 3.x 中返回一个迭代器




##读取文件
##使用 with open 语法来读取文件。它将会为您自动关闭文件。




##行的延续

##糟糕:
my_very_big_string = """For a long time I used to go to bed early. Sometimes, \
    when I had put out my candle, my eyes would close so quickly that I had not even \
    time to say “I’m going to sleep.”"""


##优雅
my_very_big_string = (
    "For a long time I used to go to bed early. Sometimes, "
    "when I had put out my candle, my eyes would close so quickly "
    "that I had not even time to say “I’m going to sleep.”"
)




