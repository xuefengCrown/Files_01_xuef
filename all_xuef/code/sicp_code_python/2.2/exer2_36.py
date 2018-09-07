"""
exer2.36 accumulate_n
((1 2 3) (4 5 6) (7 8 9) (10 11 12))-->(22 26 30)

"""

import exer2_33 as funcs
import accumulate as accu
import operator as oper

def accumulate_n(op, init, seqs):
    # 每个序列等长度，所以如果第一个处理完了，意味着都处理完了
    if len(seqs[0])==0: return []
    return funcs._append([accu.accumulate(op,
                                         init,
                                         list(map(lambda seq:seq[0], seqs)))],
                         accumulate_n(op,
                                      init,
                                      list(map(lambda seq:seq[1:], seqs))))

def test():
    seqs = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    print(accumulate_n(oper.add, 0, seqs))
    
if __name__ == '__main__':
    test()    
