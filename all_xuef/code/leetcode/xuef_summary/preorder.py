# -*- coding: UTF-8 -*-

"""
对文件夹操作, 要使用 os, os.path module
"""
import os

dname = "4preorder"
bn = os.path.basename
def pre(puth, depth):
    print('--'*depth + bn(puth))
    files = os.listdir(puth)
    for f in files:
        npath = puth + '\\' + f 
        if os.path.isdir(npath):
            pre(npath, depth+1)
        else: print('--'*depth + f)
        
puth = os.path.abspath("4preorder")
pre(puth, 0)

