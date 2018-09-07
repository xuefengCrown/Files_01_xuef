"""
315. Count of Smaller Numbers After Self
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller
elements to the right of nums[i].
Example:
    Input: [5,2,6,1]
    Output: [2,1,1,0] 
Explanation:
    To the right of 5 there are 2 smaller elements (2 and 1).
    To the right of 2 there is only 1 smaller element (1).
    To the right of 6 there is 1 smaller element (1).
    To the right of 1 there is 0 smaller element.
Solution:
BIT: 索引+压缩 思想
当涉及到顺序统计时, 索引方法比较有效
"""
def countSmaller(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    uniques = list(set(nums))
    uniques.sort() # 最好sort下,因为没sort;leetcode提交多次都没通过
    ranks = {i:idx+1 for idx,i in enumerate(uniques)}
    print(ranks)
    freq, res = [0]*(len(ranks)+1), []
    for i in reversed(nums):
        print(i)
        freq[ranks[i]] += 1
        res.append(sum(freq[:ranks[i]]))

    return list(reversed(res))
    
nums = [5,2,2,6,1]
nums = [-1,-2]
rs = countSmaller(nums)

print(rs)
