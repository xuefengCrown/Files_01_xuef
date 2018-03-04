"""
实现有理数系统
python3.6
author: xuef
"""
from rational2 import *

def add_rat(x, y):
    numer_x, numer_y = numer(x), numer(y)
    denom_x, denom_y = denom(x), denom(y)
    return make_rat(numer_x * denom_y + numer_y * denom_x, denom_x * denom_y)
    
def mul_rat(x, y):
    numer_x, numer_y = numer(x), numer(y)
    denom_x, denom_y = denom(x), denom(y)
    return make_rat(numer_x * numer_y, denom_x * denom_y)
    

one_half = make_rat(1, 2)
one_third = make_rat(1, 3)
one_fourth = make_rat(1, 4)
print_rat(add_rat(one_half, one_fourth))

#print(gcd(1997, 615))











