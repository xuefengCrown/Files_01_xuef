
def compose(f, g):
    def h(x):
        return f(g(x))
    return h

#The following definition is correct,
#but many programmers have trouble understanding it quickly.
compose2 = lambda f,g: (lambda x: f(g(x)))

inc1 = lambda x: x+1
square = lambda x: x*x

p=print
fg1=compose(square, inc1)
fg2=compose2(square, inc1)

p(fg1(8))
p(fg2(8))
