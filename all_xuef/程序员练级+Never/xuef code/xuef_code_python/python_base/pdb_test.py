
"""
注意：你的文件名不能叫 pdb.py(这是pdb模块的名字)
"""
import pdb

def sam(a, b):
    r = a+b
    print(r)
    return r

a=1
b=2

pdb.set_trace()
print("-"*10)
sam(a,b)
