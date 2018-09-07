
nums = [4,3,2,7,8,2,3,1]
res = []
for i in nums:
    if nums[abs(i)-1] < 0:
        res.append(abs(i))
    nums[abs(i)-1] *= -1
    
print(res)
