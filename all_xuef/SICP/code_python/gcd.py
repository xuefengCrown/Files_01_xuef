
# 欧几里得算法求a, b 的最大公约数
def gcd(a, b):
    if a%b == 0: return b
    return gcd(b, a%b)

