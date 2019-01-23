
def cond():
    x = 3
    if x < 5:
        return "yes"
    else:
        return "no"
    
"""
>>> dis.dis(cond)
  2           0 LOAD_CONST               1 (3)
              3 STORE_FAST               0 (x)
 
  3           6 LOAD_FAST                0 (x)
              9 LOAD_CONST               2 (5)
             12 COMPARE_OP               0 (<)
             15 POP_JUMP_IF_FALSE       22
 
  4          18 LOAD_CONST               3 ('yes')
             21 RETURN_VALUE
 
  6     >>   22 LOAD_CONST               4 ('no')
             25 RETURN_VALUE
             26 LOAD_CONST               0 (None)
             29 RETURN_VALUE
"""
#line-num    字节索引 指令名            指令参数 (关于参数是什么的提示)


#Explore Bytecode
##我鼓励你用dis.dis来试试你自己写的函数。一些有趣的问题值得探索：
"""
1. 对解释器而言for循环和while循环有什么不同？
2. 能不能写出两个不同函数，却能产生相同的字节码?
3. elif是怎么工作的？列表推导呢？
"""

import dis

dis.dis(cond)
