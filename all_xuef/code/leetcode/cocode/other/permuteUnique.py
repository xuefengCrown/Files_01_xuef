
"""
46 Permutations unique
"""
def permuteUnique(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def perm(perms, n):
        return {tuple(p[0:idx]+[n]+p[idx:]):p[0:idx]+[n]+p[idx:] for p in perms.values() for idx in range(len(p)+1)}

    def pUnique(lst):
        if len(lst) == 1: return {tuple(lst): lst}
        return perm(pUnique(lst[:-1]), lst[-1])
    return list(pUnique(nums).values())

print(permuteUnique([1, 2, 1, 2]))
