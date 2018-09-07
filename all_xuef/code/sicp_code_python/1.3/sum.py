
def sum_(term, next_v, a, b):
    "高阶sum，递归版本"
    if a > b:
        return 0
    else:
        return term(a) + sum_(term, next_v, next_v(a), b)
def sum_iter(term, next_v, a, b):
    "高阶sum，迭代版本"
    def iter_help(a, result):
        if a > b: return result
        else:
            return iter_help(next_v(a), result+term(a))
    return iter_help(a, 0)

