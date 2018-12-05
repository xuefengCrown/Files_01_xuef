
#检查字符串开头或结尾的一个简单方法是使用 str.startswith() 或者是 str.endswith() 方法。

#如果你想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去，
#然后传给 startswith() 或者 endswith() 方法：

name='xxx.c'
print(name.endswith(('.c', '.h')))

from urllib.request import urlopen
def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()
