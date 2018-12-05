# 要成为高手，需要洞悉一切细节!
"""
1. 对于简单的字面模式，直接使用 str.replace() 方法
2. 复杂模式，使用 re.sub
"""

#假设你想将形式为 11/27/2012 的日期字符串改成 2012-11-27 。示例如下：

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
p=print
#### \3 指向前面模式的捕获组号
subed = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
#'Today is 2012-11-27. PyCon starts 2013-3-13.'
p(subed)
statement = 'print "hello,world"'

py3sm = re.sub(r"print (.+)", r"print(\1)", statement)
p(py3sm)

# 如果你打算用相同的模式做多次替换，考虑先编译它来提升性能。

#对于更加复杂的替换，可以传递一个替换回调函数来代替
## 回调函数的协议
#### 一个替换回调函数的参数是一个 match 对象，也就是 match() 或者 find() 返回的对象。
#### 使用 group() 方法来提取特定的匹配部分。回调函数最后返回替换字符串。


#如果除了替换后的结果外，你还想知道有多少替换发生了，可以使用 re.subn() 来代替。比如:
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
newtext, n = datepat.subn(r'\3-\1-\2', text)
p(newtext)
#'Today is 2012-11-27. PyCon starts 2013-3-13.'
p(n)
#2

