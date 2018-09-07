def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    """
    # 1 is an ugly number
    ugly_nums = [1]
    # An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
    # 通过2(or 3, 5)与已经生成的ugly number相乘来生成新的ugly number;
    # 相当于有3个生成器(2,3,5), i2, i3, i5用来标记流水线位置
    i2,i3,i5 = 0,0,0
    
    while n > 1:
        # 每个generator都生产一个新数; 其中最小的就是下一个 ugly number
        u2, u3, u5 = 2*ugly_nums[i2], 3*ugly_nums[i3], 5*ugly_nums[i5]
        next_ugly = min(u2,u3,u5)
        # 注意: u2,u3,u5 可能存在重复值,得过滤掉;
        if u2==next_ugly: i2 += 1
        if u3==next_ugly: i3 += 1
        if u5==next_ugly: i5 += 1
        n -= 1
        ugly_nums.append(next_ugly)
    return ugly_nums[-1]

print(nthUglyNumber(100))
