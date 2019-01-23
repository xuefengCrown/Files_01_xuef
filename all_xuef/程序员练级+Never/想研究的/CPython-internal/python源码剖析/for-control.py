
sc = """
lst = [1, 2]

for i in lst:
    print(i)
"""

import dis

dis.dis(sc)
"""
  2           0 LOAD_CONST               0 (1)
              2 LOAD_CONST               1 (2)
              4 BUILD_LIST               2
              6 STORE_NAME               0 (lst)

  4           8 SETUP_LOOP              20 (to 30)
             10 LOAD_NAME                0 (lst)
             12 GET_ITER
        >>   14 FOR_ITER                12 (to 28)
             16 STORE_NAME               1 (i)

  5          18 LOAD_NAME                2 (print)
             20 LOAD_NAME                1 (i)
             22 CALL_FUNCTION            1
             24 POP_TOP
             26 JUMP_ABSOLUTE           14
        >>   28 POP_BLOCK
        >>   30 LOAD_CONST               2 (None)
             32 RETURN_VALUE

"""

#SETUP_LOOP实现中，仅是简单调用了 PyFrame_BlockSetup函数
"""
[frameobject.c]
void PyFrame_BlockSetup(PyFrameObject *f, int type, int handler, int level) {
  PyTryBlock *b;
  b = &f->f_blockstack[f_iblock++];
  b->b_type = type;
  b->b_level = level;
  b->b_handler = handler;
}

[frameobject.h]
typedef struct _frame {
  ...
  int f_iblock; /* index in f_blockstack */
  PyTryBlock f_blockstack[CO_MAXBLOCKS]; /* for try and loop blocks */
  ...
} PyFrameObject;


typedef struct {
  int b_type;  //what kind of block this is
  int b_handler; // where to jump to find handler
  int b_level; //value stack level to pop to
} PyTryBlock;
"""

##10.2.4 终止迭代
"""
FOR_ITER 指令负责
"""






















