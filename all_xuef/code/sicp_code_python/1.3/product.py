
def product(term, next_v, a, b):
    "函数在各个点的乘积，递归版本"
    if a > b:
        return 1
    else:
        return term(a) * product(term, next_v, next_v(a), b)
def product_iter(term, next_v, a, b):
    "迭代版本"
    def iter_help(a, result):
        if a > b: return result
        else:
            return iter_help(next_v(a), result*term(a))
    return iter_help(a, 1)

print(product_iter((lambda x: x), (lambda n: n+1), 1, 5))
