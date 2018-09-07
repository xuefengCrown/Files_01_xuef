
"""
exer2.34
对于x的某个给定值，求出一个多项式在x处的值;
采用著名的Horner规则，
假定多项式的系数安排在一个序列里，从 a0直至an:
1 + 3x + 5x^3 + x^5
[1, 3, 0, 5, 0, 1]
"""
import operator as op
import accumulate as accu

def horner_eval(x, coefficient_sequence):
    return accu.accumulate(lambda this_coeff,higher_terms:this_coeff + op.mul(x, higher_terms),
                           0,
                           coefficient_sequence)

def test():
    seq, x = [1, 3, 0, 5, 0, 1], 2
    print(horner_eval(x, seq))

if __name__ == "__main__":
    test()
