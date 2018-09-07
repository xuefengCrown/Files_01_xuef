## intro

dynamic programming 是一种设计技巧



## example

### longest common subsequence

最长公共子序列

```
给定两个序列， x[1, m], y[1, n]
找出它们的最长公共子序列
x: A B C B D A B
y: B D C A B A
BDAB, BCAB, BCBA
```

### brute force

给定子串，check它是否是y的子串，所需时间为 O(n)

x 的子序列数量为 2^m（排列组合的重要，以及《离散数学及其应用》）

### 简化

1. look at length of LCS(x, y)
2. extend the alg to find LCS itself

Notation: |s| denotes length of seq s

Strategy: consider prefixes of x and y

Define c[i, j] = |LCS(x[1, i], y[1, j])|

we're going to calculate all c[i, j] for all ij

```
c[i, j] = {
  c[i-1, j-1] , if x[i] = y[j]
  max{c[i, j-1], c[i-1, j]}, otherwise
}
还是得看普林斯顿《具体数学》，和《算法引论：一种创造性方法》
```

```
proof:
case, x[i] = y[j]
let z[1, k] = LCS(x[1, i], y[1, j]), where c[i, j] = k.
then, z[k] = ?(x[i] also y[j])
我很快回答出这个问题。突然感觉我好强啊!
```

### 动态规划问题的特征

1. 最优子结构 Optional substructure



```
If z=LCS(x, y), then any prefix of z is an LCS of a prefix of x and a prefix of y.
```

2. overlapping subproblems

重叠子问题（a recursive solution contains a small number distinct subproblems repeated many times）

memo-ization algorithm（not memorization）

### dynamic programming

除了上面的自顶向下的计算思路

我们也可以自底向上的计算表格

### Recursive alg for LCS

```
LCS(x, y, i, j) // ignoring basecases
	if x[i] = y[j]
		then c[i, j] <-- LCS(x, y, i-1, j-1)
	else c[i, j] <-- max{
    	LCS(x, y, i-1, y),
    	LCS(x, y, i, y-1)
	}
	return c[i, j]
```

#### 最坏情况



#### 程序的递归树







