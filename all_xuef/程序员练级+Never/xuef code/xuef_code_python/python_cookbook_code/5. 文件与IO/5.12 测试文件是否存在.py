
# 文件指的是什么? 本质上是躺在磁盘某处的一段而进制数据
# 文件的属性有哪些?
## 1. 文件名和文件类型这些第二属性
## 2. 文件本身的内容，我称之为第一属性
## 3. 文件元数据(比如文件大小或者是修改日期)
## 4. 文件的权限(操作系统加给文件的属性)
"""
>>> import os
>>> os.path.exists('/etc/passwd')
True
>>> os.path.exists('/tmp/spam')
False
>>>
"""

# 文件类型侦测
## regular file, directory, symbolic link
"""
>>> # Is a regular file
>>> os.path.isfile('/etc/passwd')
True

>>> # Is a directory
>>> os.path.isdir('/etc/passwd')
False

>>> # Is a symbolic link
>>> os.path.islink('/usr/local/bin/python3')
True

>>> # Get the file linked to
>>> os.path.realpath('/usr/local/bin/python3')
'/usr/local/bin/python3.3'
>>>
"""

# 获取文件元数据(比如文件大小或者是修改日期)
"""
>>> os.path.getsize('/etc/passwd')
3669
>>> os.path.getmtime('/etc/passwd')
1272478234.0
>>> import time
>>> time.ctime(os.path.getmtime('/etc/passwd'))
'Wed Apr 28 13:10:34 2010'
>>>
"""

# 文件权限
"""
使用 os.path 来进行文件测试是很简单的。 在写这些脚本时，可能唯一需要注意的就是
你需要考虑文件权限的问题，特别是在获取元数据时候。
"""











