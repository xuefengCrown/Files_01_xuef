def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    """
    def merge2list(f, s):
        if len(f) == 0:
            return s
        if len(s) == 0:
            return f
        if f[0] < s[0]:
            return [f[0]] + merge2list(f[1:], s)
        elif f[0] > s[0]:
            return [s[0]] + merge2list(f, s[1:])
        else:
            return [f[0]] + merge2list(f[1:], s[1:])
    # l1, l2, l3 is sorted list
    def merge(l1, l2, l3):    
        l12 = merge2list(l1, l2)
        l123 = merge2list(l12, l3)
        return l123         
                
    ugly_nums = [1]
    cnt = 0
    while True:
        # An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
        L1 = [2*i for i in ugly_nums]
        L2 = [3*i for i in ugly_nums]
        L3 = [5*i for i in ugly_nums]
        cnt = cnt+3
        ugly_nums = merge2list(ugly_nums, merge(L1, L2, L3))[:cnt]
        print(ugly_nums)
        
        if cnt >= n:
            break

    return ugly_nums[n-1]
num = nthUglyNumber(41)
print(num)





