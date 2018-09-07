def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    rs = 0
    for i in range(1, 33):
        rs += n & 1 # n & 1 获取最低位
        n = n >> 1
    return rs

n=  2147483648 # (10000000000000000000000000000000)
#n=128
rs=hammingWeight(n)
print(rs)
