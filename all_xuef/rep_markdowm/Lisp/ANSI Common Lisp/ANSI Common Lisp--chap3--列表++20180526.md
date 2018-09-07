# chap3

本章描述了你可以用列表所做的很多事情，以及使用它们来演示一些普遍的 Lisp 概念。

## 3.1 构造 (Conses)

如果参数是一个 *Cons* 对象，函数 `consp` 返回真。所以我们可以这样定义 `listp` :

```
(defun our-listp (x)
  (or (null x) (consp x)))
```

因为所有不是 *Cons* 对象的东西，就是一个原子 (atom)，判断式 `atom` 可以这样定义：

```
(defun our-atom (x) (not (consp x)))

```

注意， `nil` 既是一个原子，也是一个列表。

## 3.2 相等性 (Equality)

每一次你调用 `cons` 时， Lisp 会配置一块新的内存给两个指针。所以如果我们用同样的参数调用 `cons` 两次，我们得到两个数值看起来一样，但实际上是两个不同的对象：

```
> (eql (cons 'a nil) (cons 'a nil))
NIL

```

如果我们也可以询问两个列表是否有相同元素，那就很方便了。 Common Lisp 提供了这种目的另一个判断式： `equal` 。而另一方面 `eql` 只有在它的参数是相同对象时才返回真，

本质上 `equal` 若它的参数打印出的值相同时，返回真：

```
> (equal x (cons 'a nil))
T

```

这个判断式对非列表结构的别种对象也有效，但一种仅对列表有效的版本可以这样定义：

```
> (defun our-equal (x y)
    (or (eql x y)
        (and (consp x)
             (consp y)
             (our-equal (car x) (car y))
             (our-equal (cdr x) (cdr y)))))

```

这个定义意味着，如果某个 `x` 和 `y` 相等( `eql` )，那么他们也相等( `equal` )。

**勘误:** 这个版本的 `our-equal` 可以用在符号的列表 (list of symbols)，而不是列表 (list)。

## 3.3 为什么 Lisp 没有指针

```
> (setf x '(a b c))
(A B C)
> (setf y x)
(A B C)
```



## 3.4 建立列表 (Building Lists)

函数 `copy-list` 接受一个列表，然后返回此列表的复本。新的列表会有同样的元素，但是装在新的 *Cons* 对象里：

```
> (setf x '(a b c)
        y (copy-list x))
(A B C)
```

我们可以把 `copy-list` 想成是这么定义的：

```
(defun our-copy-list (lst)
 (if (atom lst)
     lst
     (cons (car lst) (our-copy-list (cdr lst)))))
```

最后，函数 `append` 返回任何数目的列表串接 (concatenation)：

```
> (append '(a b) '(c d) 'e)
(A B C D . E)

```

通过这么做，它复制所有的参数，除了最后一个



## 3.7 映射函数 (Mapping Functions)

Common Lisp 提供了数个函数来对一个列表的元素做函数调用。最常使用的是 `mapcar` ，接受一个函数以及一个或多个列表，并返回把函数应用至每个列表的元素的结果，直到有的列表没有元素为止：

```
> (mapcar #'(lambda (x) (+ x 10))
          '(1 2 3))
(11 12 13)

> (mapcar #'list
          '(a b c)
          '(1 2 3 4))
((A 1) (B 2) (C 3))

```

相关的 `maplist` 接受同样的参数，将列表的渐进的下一个 `cdr` 传入函数。

```
> (maplist #'(lambda (x) x)
           '(a b c))
((A B C) (B C) (C))
```

## 3.8 树 (Trees)

*Cons* 对象可以想成是二叉树， `car` 代表左子树，而 `cdr` 代表右子树。

Common Lisp 有几个内置的操作树的函数。举例来说， `copy-tree` 接受一个树，并返回一份副本。它可以这么定义：

```
(defun our-copy-tree (tr)
  (if (atom tr)
       tr
       (cons (our-copy-tree (car tr))
             (our-copy-tree (cdr tr)))))
```

把这跟 36 页的 `copy-list` 比较一下； `copy-tree` 复制每一个 *Cons* 对象的 `car` 与 `cdr` ，而 `copy-list` 仅复制 `cdr` 。



没有内部节点的二叉树没有太大的用处。 Common Lisp 包含了操作树的函数，不只是因为我们需要树这个结构，而是因为我们需要一种方法，来操作列表及所有内部的列表。举例来说，假设我们有一个这样的列表：

```
(and (integerp x) (zerop (mod x 2)))
```

而我们想要把各处的 `x` 都换成 `y` 。调用 `substitute` 是不行的，它只能替换序列 (sequence)中的元素：

```
> (substitute 'y 'x '(and (integerp x) (zerop (mod x 2))))
(AND (INTEGERP X) (ZEROP (MOD X 2)))
```

这个调用是无效的，因为列表有三个元素，没有一个元素是 `x` 。我们在这所需要的是 `subst` ，它替换树之中的元素。

```
> (subst 'y 'x '(and (integerp x) (zerop (mod x 2))))
(AND (INTEGERP Y) (ZEROP (MOD Y 2)))

```

如果我们定义一个 `subst` 的版本，它看起来跟 `copy-tree` 很相似：

```
(and (integerp x) (zerop (mod x 2)))

> (defun our-subst (new old tree)
    (if (eql tree old)
        new
        (if (atom tree)
            tree
            (cons (our-subst new old (car tree))
                  (our-subst new old (cdr tree))))))
```

操作树的函数通常有这种形式， `car` 与 `cdr` 同时做递归。这种函数被称之为是 *双重递归* (doubly recursive)。

### 理解递归

递归的优点是它精确地让我们更抽象地来设计算法。你不需要考虑真正函数时所有的调用过程，就可以判断一个递归函数是否是正确的。

要知道一个递归函数是否做它该做的事，你只需要问，它包含了所有的情况吗？举例来说，下面是一个寻找列表长度的递归函数：

```
> (defun len (lst)
    (if (null lst)
        0
        (+ (len (cdr lst)) 1)))

```

我们可以借由检查两件事情，来确信这个函数是正确的：

1. 对长度为 `0` 的列表是有效的。
2. 给定它对于长度为 `n` 的列表是有效的，它对长度是 `n+1` 的列表也是有效的。

如果这两点是成立的，我们知道这个函数对于所有可能的列表都是正确的。



更复杂的递归函数，可能会有更多的情况需要讨论，但是流程是一样的。举例来说， 41 页的 `our-copy-tree` ，我们需要讨论三个情况： 原子，单一的 *Cons* 对象， `n+1` 的 *Cons* 树。



能够判断一个递归函数是否正确只不过是理解递归的上半场，下半场是能够写出一个做你想做的事情的递归函数。



## 3.10 集合 (Sets)

列表是表示小集合的好方法。列表中的每个元素都代表了一个集合的成员：

```
> (member 'b '(a b c))
(B C)

```

当 `member` 要返回“真”时，与其仅仅返回 `t` ，它返回由寻找对象所开始的那部分。逻辑上来说，一个 *Cons* 扮演的角色和 `t` 一样，而经由这么做，函数返回了更多资讯。

一个 `member` 函数所接受的关键字参数是 `:test` 参数。

如果你在调用 `member` 时，传入某个函数作为 `:test` 参数，那么那个函数就会被用来比较是否相等，而不是用 `eql` 。所以如果我们想找到一个给定的对象与列表中的成员是否相等( `equal` )，我们可以：

```
> (member '(a) '((a) (z)) :test #'equal)
((A) (Z))

```

关键字参数总是选择性添加的。如果你在一个调用中包含了任何的关键字参数，他们要摆在最后; 如果使用了超过一个的关键字参数，摆放的顺序无关紧要。

另一个 `member` 接受的关键字参数是 `:key` 参数。借由提供这个参数，你可以在作比较之前，指定一个函数运用在每一个元素：

```
> (member 'a '((a b) (c d)) :key #'car)
((A B) (C D))

```

在这个例子里，我们询问是否有一个元素的 `car` 是 `a` 。

如果我们想要找到一个元素满足任意的判断式像是── `oddp` ，奇数返回真──我们可以使用相关的 `member-if` ：

```
> (member-if #'oddp '(2 3 4))
(3 4)

```

我们可以想像一个限制性的版本 `member-if` 是这样写成的：

```
(defun our-member-if (fn lst)
  (and (consp lst)
       (if (funcall fn (car lst))
           lst
           (our-member-if fn (cdr lst)))))

```

函数 `adjoin` 像是条件式的 `cons` 。它接受一个对象及一个列表，如果对象还不是列表的成员，才构造对象至列表上。

```
> (adjoin 'b '(a b c))
(A B C)
> (adjoin 'z '(a b c))
(Z A B C)

```

通常的情况下它接受与 `member` 函数同样的关键字参数。

集合论中的并集 (union)、交集 (intersection)以及补集 (complement)的实现，是由函数 `union` 、 `intersection` 以及 `set-difference` 。

这些函数期望两个（正好 2 个）列表（一样接受与 `member` 函数同样的关键字参数）。

```
> (union '(a b c) '(c b s))
(A C B S)
> (intersection '(a b c) '(b b c))
(B C)
> (set-difference '(a b c d e) '(b e))
(A C D)

```

因为集合中没有顺序的概念，这些函数不需要保留原本元素在列表被找到的顺序。举例来说，调用 `set-difference` 也有可能返回 `(d c a)` 

## 3.11 序列 (Sequences)

在 Common Lisp 里，*序列*( *sequences* )包括了列表与向量 (vectors)。本节介绍了一些可以运用在列表上的序列函数。更深入的序列操作在 4.4 节讨论。

```
> (length '(a b c))
3
```

```
> (subseq '(a b c d) 1 2)
(B)
>(subseq '(a b c d) 1)
(B C D)
```

函数 `reverse` 返回与其参数相同元素的一个序列，但顺序颠倒。

```
> (reverse '(a b c))
(C B A)
```

Common Lisp 有一个内置的排序函数叫做 `sort` 。它接受一个序列及一个比较两个参数的函数，返回一个有同样元素的序列，根据比较函数来排序：

```
> (sort '(0 2 1 3 8) #'>)
(8 3 2 1 0)

```

你要小心使用 `sort` ，因为它是*破坏性的*(*destructive*)。考虑到效率的因素， `sort` 被允许修改传入的序列。所以如果你不想你本来的序列被改动，传入一个副本。

使用 `sort` 及 `nth` ，我们可以写一个函数，接受一个整数 `n` ，返回列表中第 `n` 大的元素：

```
(defun nthmost (n lst)
  (nth (- n 1)
       (sort (copy-list lst) #'>)))
```

多努力一点，我们可以写出这个函数的一个更有效率的版本。

函数 `every` 和 `some` 接受一个判断式及一个或多个序列。当我们仅输入一个序列时，它们测试序列元素是否满足判断式：

```
> (every #'oddp '(1 3 5))
T
> (some #'evenp '(1 2 3))
T

```

如果它们输入多于一个序列时，判断式必须接受与序列一样多的元素作为参数，而参数从所有序列中一次提取一个：

```
> (every #'> '(1 3 5) '(0 2 4))
T

```

如果序列有不同的长度，最短的那个序列，决定需要测试的次数。

## 3.12 栈 (Stacks)

`(push x y)` 把 `x` 放入列表 `y` 的前端。而 `(pop x)` 则是将列表 x 的第一个元素移除，并返回这个元素。

两个函数都是由 `setf` 定义的。如果参数是常数或变量，很简单就可以翻译出对应的函数调用。

表达式

`(push obj lst)`

等同于

`(setf lst (cons obj lst))`

而表达式

`(pop lst)`

等同于

```
(let ((x (car lst)))
  (setf lst (cdr lst))
  x)

```

所以，举例来说：

```
> (setf x '(b))
(B)
> (push 'a x)
(A B)
> x
(A B)
> (setf y x)
(A B)
> (pop x)
(A)
> x
(B)
> y
(A B)
```



## 3.14 关联列表 (Assoc-lists)

用 *Cons* 对象来表示映射 (mapping)也是很自然的。一个由 *Cons* 对象组成的列表称之为*关联列表*(*assoc-list*or *alist*)。这样的列表可以表示一个翻译的集合，举例来说：

```
> (setf trans '((+ . "add") (- . "subtract")))
((+ . "add") (- . "subtract"))

```

关联列表很慢，但是在初期的程序中很方便。 Common Lisp 有一个内置的函数 `assoc` ，用来取出在关联列表中，与给定的键值有关联的 *Cons* 对：

```
> (assoc '+ trans)
(+ . "add")
> (assoc '* trans)
NIL
```

如果 `assoc` 没有找到要找的东西时，返回 `nil` 。

我们可以定义一个受限版本的 `assoc` ：

```
(defun our-assoc (key alist)
  (and (consp alist)
       (let ((pair (car alist)))
        (if (eql key (car pair))
            pair
            (our-assoc key (cdr alist))))))

```

和 `member` 一样，实际上的 `assoc` 接受关键字参数，包括 `:test` 和 `:key` 。 Common Lisp 也定义了一个 `assoc-if` 之于 `assoc` ，如同 `member-if` 之于 `member` 一样。



## 3.15 最短路径

图 3.12 包含一个搜索网络中最短路径的程序。函数 `shortest-path` 接受一个起始节点，目的节点以及一个网络，并返回最短路径，如果有的话。

在这个范例中，节点用符号表示，而网络用含以下元素形式的关联列表来表示：

*(node . neighbors)*

所以由图 3.13 展示的最小网络 (minimal network)可以这样来表示：

`(setf min '((a b c) (b c) (c d)))`

要找到从节点 `a` 可以到达的节点，我们可以：

```
> (cdr (assoc 'a min))
(B C)
```

```lisp
(defun shortest-path (start end net)
  (bfs end (list (list start)) net))

(defun bfs (end queue net)
  (if (null queue)
      nil
      (let ((path (car queue)))
        (let ((node (car path)))
          (if (eql node end)
              (reverse path)
              (bfs end
                   (append (cdr queue)
                           (new-paths path node net))
                   net))))))

(defun new-paths (path node net)
  (mapcar #'(lambda (n)
              (cons n path))
          (cdr (assoc node net))))
```

这是队列在我们连续调用 `bfs` 看起来的样子：

```
((A))
((B A) (C A))
((C A) (C B A))
((C B A) (D C A))
((D C A) (D C B A))
```

图 3.12 程序使用广度优先的方式搜索网络。要使用广度优先搜索，你需要维护一个含有未探索节点的队列。每一次你到达一个节点，检查这个节点是否是你要的。如果不是，你把这个节点的子节点加入队列的尾端，并从队列起始选一个节点，从这继续搜索。借由总是把较深的节点放在队列尾端，我们确保网络一次被搜索一层。

图 3.12 中的代码较不复杂地表示这个概念。我们不仅想要找到节点，还想保有我们怎么到那的纪录。所以与其维护一个具有节点的队列 (queue)，我们维护一个已知路径的队列，每个已知路径都是一列节点。当我们从队列取出一个元素继续搜索时，它是一个含有队列前端节点的列表，而不只是一个节点而已。

函数 `bfs` 负责搜索。起初队列只有一个元素，一个表示从起点开始的路径。所以 `shortest-path` 调用 `bfs` ，并传入 `(list (liststart))` 作为初始队列。

`bfs` 函数第一件要考虑的事是，是否还有节点需要探索。如果队列为空， `bfs` 返回 `nil` 指出没有找到路径。如果还有节点需要搜索， `bfs` 检查队列前端的节点。如果节点的 `car` 部分是我们要找的节点，我们返回这个找到的路径，并且为了可读性的原因我们反转它。如果我们没有找到我们要找的节点，它有可能在现在节点之后，所以我们把它的子节点（或是每一个子路径）加入队列尾端。然后我们递回地调用 `bfs` 来继续搜寻剩下的队列。

因为 `bfs` 广度优先地搜索，第一个找到的路径会是最短的，或是最短之一：

```
> (shortest-path 'a 'd min)
(A C D)
```

在队列中的第二个元素变成下一个队列的第一个元素。队列的第一个元素变成下一个队列尾端元素的 `cdr` 部分。

在图 3.12 的代码不是搜索一个网络最快的方法，但它给出了列表具有多功能的概念。在这个简单的程序中，我们用三种不同的方式使用了列表：我们使用一个符号的列表来表示路径，一个路径的列表来表示在广度优先搜索中的队列 [[4\]](http://acl.readthedocs.io/en/latest/zhCN/ch3-cn.html#id6) ，以及一个关联列表来表示网络本身。





















