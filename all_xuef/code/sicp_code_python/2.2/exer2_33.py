"""
exer2.33
将一些基本的表操作看作累积的定义：
map, append, length
"""
import operator as op
import accumulate as accu
def _map(proc, seq):
    return accu.accumulate(lambda x,y:op.add([proc(x)], y),
                  [],
                  seq)

def _append(seq1, seq2):
    # 这里的lambda x,y:op.add([x], y), 在lisp中只需cons
    return accu.accumulate(lambda x,y:op.add([x], y),
                  seq2,
                  seq1)

def _length(seq):
    return accu.accumulate(lambda x,y:op.add(1, y),
                  0,
                  seq)
def test():
    seq = [1,2,3]
    res = _map(lambda x:x*x, seq)
    print(res)
    print(_append(seq, res))
    print(_length(res))

if __name__ == "__main__":
    test()
