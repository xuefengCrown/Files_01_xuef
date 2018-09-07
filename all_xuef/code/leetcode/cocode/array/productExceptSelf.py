"""238. Product of Array Except Self
[a1, a2, a3, a4]
[1,         a1,         a1*a2,      a1*a2*a3]
[a2*a3*a4, a3*a4,       a4,                1]
"""
import operator as op
def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    sz = len(nums)
    l2r = [1]*sz
    r2l = [1]*sz
    t = 1
    for i in range(sz-1):
        t *= nums[i]
        l2r[i+1] *= t
    t = 1
    for i in reversed(range(sz-1)):
        t *= nums[i+1]
        r2l[i] *= t
    print(l2r, r2l)
    return list(map(op.mul, l2r, r2l))

nums = [1,2,3,4]
print(productExceptSelf(nums))
