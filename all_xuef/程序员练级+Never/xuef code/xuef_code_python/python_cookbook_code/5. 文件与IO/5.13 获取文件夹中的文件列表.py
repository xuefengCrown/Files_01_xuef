
"""
问题
你想获取文件系统中某个目录下的所有文件列表。

os.listdir()
"""

import os.path

# Get all regular files(file name)
cur_dir_path = os.getcwd()
fnames = [fname for fname in os.listdir(cur_dir_path) if
          os.path.isfile(os.path.join(cur_dir_path, fname))]

print('\n'.join(fnames))
# Get all dirs
##dirnames = [name for name in os.listdir('somedir')
##        if os.path.isdir(os.path.join('somedir', name))]


# 字符串的 startswith() 和 endswith() 方法对于过滤一个目录的内容也是很有用的。比如：
pyfiles = [name for name in os.listdir(cur_dir_path)
            if name.endswith('.py')]


# 对于文件名的匹配，你可能会考虑使用 glob 或 fnmatch 模块。比如：
"""
import glob
pyfiles = glob.glob('somedir/*.py')

from fnmatch import fnmatch
pyfiles = [name for name in os.listdir('somedir')
            if fnmatch(name, '*.py')]
"""


"""
最后还有一点要注意的就是，有时候在处理文件名编码问题时候可能会出现一些问题。
通常来讲，函数 os.listdir() 返回的实体列表会根据系统默认的文件名编码来解码。
但是有时候也会碰到一些不能正常解码的文件名。 关于文件名的处理问题，
在5.14和5.15小节有更详细的讲解。
"""
