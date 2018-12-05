
##注意，series 是 make_averager 函数的局部变量，因为那个函数的定
##义体中初始化了 series：series = []。可是，调用 avg(10)
##时，make_averager 函数已经返回了，而它的本地作用域也一去不复
##返了。
def make_averager():
    series = []
    def averager(new_value):
        #在 averager 函数中，series 是自由变量（free variable）。
        #这是一个技术术语，指未在本地作用域中绑定的变量
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager
