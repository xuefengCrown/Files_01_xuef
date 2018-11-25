

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
# 数据过滤
filtered = [n for n in mylist if n > 0]

clip_neg = [n if n > 0 else 0 for n in mylist]

# 过滤 + 转换数据
import math
sqrts = [math.sqrt(n) for n in mylist if n > 0]










