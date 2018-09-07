"""
179. Largest Number
有时候你可以换个角度看问题，重写代码以排除特例，完美覆盖所有情况，那才是好的代码，
同时也是简单的代码。其实这些都不重要，代码的细节不重要，重要的是你一定要有好的品味。
好的品味可以体现在更长的代码中，好的品味体现在能看清全局，甚至有一种直觉，知道怎么
把事情做的更漂亮！--Linus Torvalds

"""
# python2.7
def largestNumber(nums):
    """
    :type nums: List[int]
    :rtype: str
    """ 
    return ''.join(sorted(list(map(str, nums)), lambda a,b:cmp(b+a, a+b))) if len(nums)!=nums.count(0) else "0"

nums = [3,30,34,5,9]
largestNumber(nums)
