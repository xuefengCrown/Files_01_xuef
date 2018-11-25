

"""
全局变量只要没改→就不用加global
"""

num=100
nums=[1,2]
def changeNum():
    global num
    num=200
    
def changeLst():
    nums.append(3)
    # nums=[10,20,30] 此时必须要用 global声明

print(num)
print(nums)
changeNum()
changeLst()
print(num)
print(nums)  
