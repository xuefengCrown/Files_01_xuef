"""
打印指定目录下的文件结构(python3.6) xuef,201811
"""
import os,sys

SPACES = 1 #层次间隔

# 处理有问题的文件名编码
def bad_filename(filename):
    temp = filename.encode(sys.getfilesystemencoding(), errors='surrogateescape')
    return temp.decode('latin-1')
def good_print(s):
    try:
        print(s)
    except UnicodeEncodeError:
        print(bad_filename(s))
        
def walk(d, prestr):
    """ 顺序输出目录d下所有文件, 对于目录, 继续walk之 """
    abspath = os.path.abspath(d)
    dirname = os.path.basename(abspath)
    prestr += ' '*SPACES + '|'
    print(prestr, '-', dirname, sep='')
    files =  os.listdir(d)
    for f in files:
        f_abspath = os.path.join(abspath, f)
        if os.path.isdir(f_abspath):
            walk(f_abspath, prestr)
        else:
            print(prestr + ' '*SPACES, '|-', sep='', end='')
            good_print(f)
walk('.', '') # 打印当前目录下的文件层次结构

def walker(d, saved2=None):
    with open(saved2, 'w') as f:
        sys.stdout = f
        walk(d, '')
