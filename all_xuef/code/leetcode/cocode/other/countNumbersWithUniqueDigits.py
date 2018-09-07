"""
357. Count Numbers with Unique Digits (dp)
Given a non-negative integer n, count all numbers with unique digits, x,
where 0 ≤ x < 10^n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of
0 ≤ x < 100,
excluding [11,22,33,44,55,66,77,88,99])

"""
import itertools as it
def countNumbersWithUniqueDigits(n):
    """
    :type n: int
    :rtype: int
    """
    def insert_digit(s):
        # insert 0~9
        s2 = set()
        for ele in s:
            for n in range(10):
                print([i for i in it.permutations(ele + (n,)) if i[0] != 0])
                s2.update([i for i in it.permutations(ele + (n,)) if i[0] != 0])
        return s2

    if n==2: return 91
    non_unique = 9
    s = set([(i,i) for i in range(1, 10)])
    #print(s)
    for i in range(3, n+1):
        s2 = insert_digit(s)
        s = s2
        non_unique += len(s)
    print(len(s))    
    return 10**n - non_unique
    
print(countNumbersWithUniqueDigits(3))
