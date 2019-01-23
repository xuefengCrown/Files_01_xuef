
##Python中的异常控制语义结构
sc = """
try:
    raise Exception('i am a exception')
except Exception(e):
    print(e)
finally:
    print('finally code')
"""
import dis
dis.dis(sc)
"""
  2           0 SETUP_FINALLY           50 (to 52)
              2 SETUP_EXCEPT            12 (to 16)

  3           4 LOAD_NAME                0 (Exception)
              6 LOAD_CONST               0 ('i am a exception')
              8 CALL_FUNCTION            1
             10 RAISE_VARARGS            1
             12 POP_BLOCK
             14 JUMP_FORWARD            32 (to 48)

  4     >>   16 DUP_TOP
             18 LOAD_NAME                0 (Exception)
             20 LOAD_NAME                1 (e)
             22 CALL_FUNCTION            1
             24 COMPARE_OP              10 (exception match)
             26 POP_JUMP_IF_FALSE       46
             28 POP_TOP
             30 POP_TOP
             32 POP_TOP

  5          34 LOAD_NAME                2 (print)
             36 LOAD_NAME                1 (e)
             38 CALL_FUNCTION            1
             40 POP_TOP
             42 POP_EXCEPT
             44 JUMP_FORWARD             2 (to 48)
        >>   46 END_FINALLY
        >>   48 POP_BLOCK
             50 LOAD_CONST               1 (None)

  7     >>   52 LOAD_NAME                2 (print)
             54 LOAD_CONST               2 ('finally code')
             56 CALL_FUNCTION            1
             58 POP_TOP
             60 END_FINALLY
             62 LOAD_CONST               1 (None)
             64 RETURN_VALUE
"""
    
