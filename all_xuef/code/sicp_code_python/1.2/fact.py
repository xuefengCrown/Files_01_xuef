"""
线性递归与迭代
"""

def fac_iter(N, counter, product):
    "迭代法计算阶乘"
    if counter == N+1:
        return product
    else:
        return fac_iter(N, counter+1, product*counter)
def factorial(N):
    return fac_iter(N, 1, 1)

print(factorial(6))
