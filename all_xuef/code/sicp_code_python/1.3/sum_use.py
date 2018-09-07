from sum import sum_, sum_iter

def square_sum(a, b):
    def term(x):
        return x*x
    def next_v(a):
        return a+1
    return sum_iter(term, next_v, a, b)

def pi_sum(a, b):
    "有递归深度限制，且收敛很慢"
    def term(n):
        return 1.0/(n * (n+2))
    def next_v(n):
        return n+4
    return 8*sum_iter(term, next_v, a, b)

def integral(f, a, b, dx):
    "f 在a，b间的定积分"
    def add_dx(x):
        return x + dx
    return dx*sum_(f, add_dx, a+dx/2.0, b)
print(pi_sum(1, 2000))
print(integral((lambda x:x*x*x), 0, 1, 0.01))
