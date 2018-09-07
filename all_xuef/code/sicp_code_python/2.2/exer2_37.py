"""
基本的矩阵和向量运算：
我们将向量表示为数的序列;
将矩阵表示为向量的序列;
[
    [1,2,3,4],
    [4,5,6,6],
    [6,7,8,9]
]
"""
import operator as op
import accumulate as ac
import exer2_36 as accu_n # 引入 accumulate_n

# dot-product 点积
def dot_product(v, w):
    return ac.accumulate(op.add,
                         0,
                         list(map(op.mul, v, w)))

def matrix_mul_vector(m, v):
    return list(map(lambda w:dot_product(w,v), m))

# 矩阵转置
def transpose(mat):
    return accu_n.accumulate_n(lambda x,y:[x]+y,
                               [],
                               mat)
def matrix_mul_matrix(m, n):
    cols = transpose(n)
    return list(map(lambda v: matrix_mul_vector(cols, v), m))

def test():
    v, w = [1,2,3,4], [1,2,3,4]
    m = [[1,2,3,4],
        [4,5,6,6],
        [6,7,8,9]]
    print(dot_product(v, w))
    print(matrix_mul_vector(m, v))
    print(transpose(m))
def test_mmm():
    m, n = [[1,1],[1,1]], [[1,2],[1,2]]
    print(matrix_mul_matrix(m, n))
if __name__ == '__main__':
    test_mmm()
    
