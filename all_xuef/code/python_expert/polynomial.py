#coding:utf-8

# python data model
# top-level function or top-level syntax -> corresponding __
# x + y     -> __add__
# init x    -> __init__
# repr(x)   -> __repr__
# x()       -> __call__



class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)

    def __add__(self, other):
        return Polynomial(*[x+y for x, y in zip(self.coeffs, other.coeffs)])

    def __len__(self):
        return len(self.coeffs)
    
p1, p2 = Polynomial(1,2,3), Polynomial(2,4,5)

print(p1)
print(p2)
print(p1+p2)

