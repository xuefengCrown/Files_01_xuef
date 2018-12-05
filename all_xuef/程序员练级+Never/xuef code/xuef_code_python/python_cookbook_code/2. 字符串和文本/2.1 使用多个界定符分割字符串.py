
#当你需要更加灵活的切割字符串的时候，最好使用 re.split() 方法：


line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
# r'[;,\s]\s*' 表示: 分隔符可以是逗号，分号或者是空格，并且后面紧跟着任意个的空格。
ret= re.split(r'[;,\s]\s*', line) # returning a list containing the resulting substrings.
#['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
p=print

p(ret)
##p('-'*20)
##
##p(help(re.split))


## 当你使用 re.split() 函数时候，需要特别注意的是正则表达式中是否包含一个括号捕获分组。
## 如果使用了捕获分组，那么被匹配的文本也将出现在结果列表中。

fields = re.split(r'(;|,|\s)\s*', line)
#['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']

## 如果你不想保留分割字符串到结果列表中去，但仍然需要使用到括号来分组正则表达式的话，
## 确保你的分组是非捕获分组，形如 (?:...) 。比如：

re.split(r'(?:,|;|\s)\s*', line)
## ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
