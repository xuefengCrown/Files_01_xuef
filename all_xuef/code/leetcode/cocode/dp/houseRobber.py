
def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    tab = {}
    def hr(nums, start, end):
        if start+1 >= end: return max(nums[start:end+1])
        if start in tab: return tab[start]
        # 抢或者不抢第一家
        mux = max(nums[start]+hr(nums, start+2, end), hr(nums, start+1, end))
        tab[start] = mux
        return mux
    return hr(nums,0, len(nums)-1)

nums = [1,1,3,6,7,10,7,1,8,5,9,1,4,4,3]
#nums = [82,217,170,215,153,55,185,55,185,232,69,131,130,102] # 1082
rs = rob(nums)
print(rs)
