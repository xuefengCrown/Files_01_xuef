## Intro

## Exercise

### 实现 Set



### 实现 优先队列



## 好书好课

```
《算法设计》
《算法设计手册》
《算法设计与分析基础》
《算法基础》
《如何解题》
《SICP》
《算法引论》
《算法导论》
《离散数学及其应用》
《算法-Java》
《概率论及其应用》
《Python Cookbook》
http://python3-cookbook-personal.readthedocs.io/zh_CN/latest/c06/p02_read-write_json_data.html
```

http://www.infoq.com/cn/articles/each-programmer-must-have-programming-books-bookcase

```
名校好课： https://zhuanlan.zhihu.com/p/24774857
CS61A 《SICP with Python》
CS61B https://www.bilibili.com/video/av16409150/?p=5
https://people.eecs.berkeley.edu/~jrs/61b/
斯坦福 《抽象编程》
《MIT-算法导论》
《MIT-人工智能》
《MIT-线性代数》
《MIT-离散数学》
伯克利《CSAPP》
```

https://github.com/prakhar1989/awesome-courses#algorithms

组合数学 https://www.bilibili.com/video/av22736338?from=search&seid=16735058077821252909

CS61A https://www.bilibili.com/video/av20538548/?p=78

https://www.bilibili.com/video/av21757858/?p=71

haskell-cis194： http://www.seas.upenn.edu/~cis194/spring13/lectures.html

资源： https://github.com/nonstriater/Learn-Algorithms

haskell资源：https://github.com/bitemyapp/learnhaskell/blob/master/guide-zh_CN.md

## Big Ideas

### 分类，寻找基



### 减小问题规模



## 解决问题的方法

### Divide&Conquer

```
merge_sort, reverse_pairs, count_of_range_sum
weighted_Interval_Schedule（job Schedule）, 
Strassen_algorithm（矩阵乘法）
https://en.wikipedia.org/wiki/Strassen_algorithm

```



### DP

### fibnacci

```
1. bottom-up, top-dpwn
2. o(n)-->o(logn) 时间复杂度
3. bottom-up + o(1)空间复杂度
```

topological sort of subproblem dependency DAG（有向无环图）

### shortest path

（注意要无环）

最短路径问题，这样想会清楚很多。（先尽量确定能够确定的）

### Backtracking

### Greedy

最小生成树，活动选择，霍夫曼编码

拟阵？

### 记忆化搜索

### 位操作

## 数据结构

### stack

### queue

### priority queue

#### operation

```
1. 查询或移除key最小者
2. any key may be inserted at any time

```

#### application

commonly used as "event queues" in simulation.

#### imp

##### Binary Heap

二叉堆的子树仍然是一个二叉堆

```
heap：
1. A complete binary tree；
2. no child has a key less than its parent's key;
```

often stored as arrays of entries by level order trasversal.

### heap

### linked list

### tree

### Binary Tree



### binary search tree

有序数组可以使用二分查找，但是插入节点低效；链表的插入操作是O(1)，但是查询很慢；

二叉搜索树集中了二者的有点，思想就是这么简单。

二叉搜索树的本质目的就是动态中维持有序性（中序遍历序列），尽量高效的！

#### 操作

```
如果只是检索，那hashtable更快；bst能够让你迅速查到最大和最小元素；此外还可以方便查找离目标元素最近的元素（大于等于67的最靠近元素）
```

##### 查找

当然你可以根据key查找，但那不是我们感兴趣的，如果只是这样，我们用hashtable就好了。

我们感兴趣的是 How to find smalles key >= k

##### 插入新元素

##### 删除

```
Supports three operations
– Insert(x): inserts a node with value x
– Delete(x): deletes a node with value x, if there is any
– Find(x): returns the node with value x, if there is any
Many extensions are possible
– Count(x): counts the number of nodes with value less than or equal to x
– GetNext(x): returns the smallest node with value ≥ x
```



#### BST invariant

对于任意节点，其左子树的key都要小于或等于它，右子树的key都要大于或等于它；

### balanced BST

#### definition

```
1. each node has at most 2 branches
2. Left branch ele are all less than or equal to label(root)
3. Right branch ele are all greater than or equal to label(root)
4. Left branch and right branch are also BSTs
```



```
Simple implementation cannot guarantee efficiency
– In worst case, tree height becomes n (which makes BST useless)
– Guaranteeing O(log n) running time per operation requires balancing of the tree (hard to implement)
– We will skip the implementation details

Use the standard library implementations
– set, map (C++)
– TreeSet, TreeMap (Java)
```



### 红黑树

### segment tree（线段树，区间树）

https://www.youtube.com/watch?v=TH9n_HVkjQM&index=2&list=PLMCXHnjXnTnuASA1NghV3Vs9J3D_ij5w2

### Fenwick Tree

```
A variant of segment trees
Supports very useful interval operations
– Set(k, x): sets the value of kth item equal to x
– Sum(k): computes the sum of items 1, . . . , k (prefix sum)
Note: sum of items i, . . . , j = Sum(j) − Sum(i − 1)
Both operations can be done in O(log n) time using O(n)
space
```



### Binary Index Tree

```
It was proposed to solve the prefix sum problem.
The idea to store partial sum in each node and get total sum by traversing the tree from leaf to root. The tree has a height of log(n).
Query: O(log(n))
Update: O(log(n))
```



### Graph

### Trie

## 搜索

### Binary Search

### DFS

### BFS





