"""
39. Combination Sum
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:
1. All numbers (including target) will be positive integers.
2. The solution set must not contain duplicate combinations.
Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
"""
def combinationSum(candidates, tar):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    def helper(candidates, tar):
        candidates = list(filter(lambda x:x <= tar, candidates))
        #print("candidates:", candidates)
        #print("tar:", tar)
        if not candidates and tar > 0: return [] # 注意这里的如何抛弃不符合条件的组合, 真的巧妙
        if tar == 0: return [[]]
        c0 = candidates[0]
        # 有c0, 没c0
        with_c0 = [[c0]+cmb for cmb in helper(candidates, tar-c0)]
        without_c0 = helper(candidates[1:], tar)
        return with_c0 + without_c0
    rs = helper(sorted(candidates), tar) # 这里已经没有重复, 但是我不知为什么
    uniques = []
    for i in rs:
        if not i in uniques: uniques.append(i)
    return uniques

candidates, tar = [2,3,6,7], 7
candidates, tar = [2,3,5], 8
rs = combinationSum(candidates, tar)
print(rs)
