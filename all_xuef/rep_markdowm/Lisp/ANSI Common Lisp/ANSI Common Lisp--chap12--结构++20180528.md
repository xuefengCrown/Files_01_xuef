3.3 节中介绍了 Lisp 如何使用指针允许我们将任何值放到任何地方。这种说法是完全有可能的，但这并不一定都是好事。

例如，一个对象可以是它自已的一个元素。这是好事还是坏事，取决于程序员是不是有意这样设计的。



## 12.1 共享结构 (Shared Structure)

多个列表可以共享 `cons` 。在最简单的情况下，一个列表可以是另一个列表的一部分。

```
> (setf part (list 'b 'c))
(B C)
> (setf whole (cons 'a part))
(A B C)
```

使用 `tailp` 判断式来检测一下。将两个列表作为它的输入参数，如果第一个列表是第二个列表的一部分时，则返回 `T` ：

```
> (tailp part whole)
T

```

我们可以把它想像成：

```
(defun our-tailp (x y)
  (or (eql x y)
      (and (consp y)
                         (our-tailp x (cdr y)))))

```

如定义所表明的，每个列表都是它自己的尾端， `nil` 是每一个正规列表的尾端。



在更复杂的情况下，两个列表可以是共享结构，但彼此都不是对方的尾端。在这种情况下，他们都有一个共同的尾端，如图 12.2 所示。我们像这样构建这种情况：

```
(setf part (list 'b 'c)
      whole1 (cons 1 part)
      whole2 (cons 2 part))
```



如果我们想避免共享结构，可以使用复制。函数 `copy-list` 可以这样定义：

```
(defun our-copy-list (lst)
   (if (null lst)
       nil
       (cons (car lst) (our-copy-list (cdr lst)))))

```

它返回一个不与原始列表共享顶层列表结构的新列表。函数 `copy-tree` 可以这样定义：

```
(defun our-copy-tree (tr)
   (if (atom tr)
        tr
        (cons (our-copy-tree (car tr))
              (our-copy-tree (cdr tr)))))

```

它返回一个连原始列表的树型结构也不共享的新列表。图 12.5 显示了对一个嵌套列表使用 `copy-list` 和 `copy-tree` 的区别。

![../_images/Figure-12.5.png](http://acl.readthedocs.io/en/latest/_images/Figure-12.5.png)



## 12.2 修改 (Modification)

为什么要避免共享结构呢？之前讨论的共享结构问题仅仅是个智力练习，到目前为止，并没使我们在实际写程序的时候有什么不同。当修改一个被共享的结构时，问题出现了。如果两个列表共享结构，当我们修改了其中一个，另外一个也会无意中被修改。

上一节中，我们介绍了怎样构建一个是其它列表的尾端的列表：

```
(setf whole (list 'a 'b 'c)
      tail (cdr whole))

```

因为 `whole` 的 `cdr` 与 `tail` 是相等的，无论是修改 `tail` 还是 `whole` 的 `cdr` ，我们修改的都是同一个 `cons` ：

```
> (setf (second tail ) 'e)
E
> tail
(B E)
> whole
(A B E)
```

同样的，如果两个列表共享同一个尾端，这种情况也会发生。

一次修改两个对象并不总是错误的。有时候这可能正是你想要的。但如果无意的修改了共享结构，将会引入一些非常微妙的 bug。Lisp 程序员要培养对共享结构的意识，并且在这类错误发生时能够立刻反应过来。当一个列表神秘的改变了的时候，很有可能是因为改变了其它与之共享结构的对象。

真正危险的不是共享结构，而是改变被共享的结构。为了安全起见，干脆避免对结构使用 `setf` (以及相关的运算，比如： `pop` ， `rplaca` 等)，这样就不会遇到问题了。如果某些时候不得不修改列表结构时，要搞清楚要修改的列表的来源，确保它不要和其它不需要改变的对象共享结构。如果它和其它不需要改变的对象共享了结构，或者不能预测它的来源，那么复制一个副本来进行改变。

当你调用别人写的函数的时候要加倍小心。除非你知道它内部的操作，否则，你传入的参数时要考虑到以下的情况：

1.它对你传入的参数可能会有破坏性的操作

2.你传入的参数可能被保存起来，如果你调用了一个函数，然后又修改了之前作为参数传入该函数的对象，那么你也就改变了函数已保存起来作为它用的对象[1]。

在这两种情况下，解决的方法是传入一个拷贝。

在 Common Lisp 中，一个函数调用在遍历列表结构 (比如， `mapcar` 或 `remove-if` 的参数)的过程中不允许修改被遍历的结构。关于评估这样的代码的重要性并没有明确的规定。



## 12.3 示例：队列 (Example: Queues)

共享结构并不是一个总让人担心的特性。我们也可以对其加以利用的。这一节展示了怎样用共享结构来表示[队列](http://zh.wikipedia.org/wiki/%E9%98%9F%E5%88%97)。队列对象是我们可以按照数据的插入顺序逐个检出数据的仓库，这个规则叫做[先进先出 (FIFO, first in, first out)](http://zh.wikipedia.org/zh-cn/%E5%85%88%E9%80%B2%E5%85%88%E5%87%BA)。

用列表表示[栈 (stack)](http://zh.wikipedia.org/wiki/%E6%A0%88)比较容易，因为栈是从同一端插入和检出。而表示队列要困难些，因为队列的插入和检出是在不同端。为了有效的实现队列，我们需要找到一种办法来指向列表的两个端。

图 12.6 给出了一种可行的策略。它展示怎样表示一个含有 a，b，c 三个元素的队列。一个队列就是一对列表，最后那个 `cons` 在相同的列表中。这个列表对由被称作头端 (front)和尾端 (back)的两部分组成。如果要从队列中检出一个元素，只需在其头端 `pop`，要插入一个元素，则创建一个新的 `cons` ，把尾端的 `cdr` 设置成指向这个 `cons`，然后将尾端指向这个新的 `cons` 。

![../_images/Figure-12.6.png](http://acl.readthedocs.io/en/latest/_images/Figure-12.6.png)

```
(defun make-queue () (cons nil nil))

(defun enqueue (obj q)
  (if (null (car q))
      (setf (cdr q) (setf (car q) (list obj)))
      (setf (cdr (cdr q)) (list obj)
            (cdr q) (cdr (cdr q))))
  (car q))

(defun dequeue (q)
  (pop (car q)))
```

图 12.7 中的代码实现了这一策略。其用法如下：

```
> (setf q1 (make-queue))
(NIL)
> (progn (enqueue 'a q1)
         (enqueue 'b q1)
         (enqueue 'c q1))
(A B C)

```

现在， `q1` 的结构就如图 12.6 那样：

```
> q1
((A B C) C)

```

从队列中检出一些元素：

```
> (dequeue q1)
A
> (dequeue q1)
B
> (enqueue 'd q1)
(C D)
```



## 12.4 破坏性函数 (Destructive Functions)

Common Lisp 包含一些允许修改列表结构的函数。为了提高效率，这些函数是具有破坏性的。虽然它们可以回收利用作为参数传给它们的 `cons` ，但并不是因为想要它们的副作用而调用它们 (**译者注：**因为这些函数的副作用并没有任何保证，下面的例子将说明问题)。

比如， `delete` 是 `remove` 的一个具有破坏性的版本。虽然它可以破坏作为参数传给它的列表，但它并不保证什么。在大多数的 Common Lisp 的实现中，会出现下面的情况：

```
> (setf lst '(a r a b i a) )
(A R A B I A)
> (delete 'a lst )
(R B I)
> lst
(A R B I)

```

正如 `remove` 一样，如果你想要副作用，应该对返回值使用 `setf` ：

```
(setf lst (delete 'a lst))
```

破坏性函数是怎样回收利用传给它们的列表的呢？比如，可以考虑 `nconc` —— `append` 的破坏性版本。[2]下面是两个参数版本的实现，其清楚地展示了两个已知列表是怎样被缝在一起的：

```
(defun nconc2 ( x y)
    (if (consp x)
        (progn
           (setf (cdr (last x)) y)
            x)
         y))

```

我们找到第一个列表的最后一个 *Cons* 核 (cons cells)，把它的 `cdr` 设置成指向第二个列表。一个正规的多参数的 `nconc` 可以被定义成像附录 B 中的那样。

函数 `mapcan` 类似 `mapcar` ，但它是用 `nconc` 把函数的返回值 (必须是列表) 拼接在一起的：

```
> (mapcan #'list
          '(a b c)
          '(1 2 3 4))
( A 1 B 2 C 3)

```

这个函数可以定义如下：

```
(defun our-mapcan (fn &rest lsts )
       (apply #'nconc (apply #'mapcar fn lsts)))

```

使用 `mapcan` 时要谨慎，因为它具有破坏性。它用 `nconc` 拼接返回的列表，所以这些列表最好不要再在其它地方使用。



?????????????????????????????

这类函数在处理某些问题的时候特别有用，比如，收集树在某层上的所有子结点。如果 `children` 函数返回一个节点的孩子节点的列表，那么我们可以定义一个函数返回某节点的孙子节点的列表如下：

```
(defun grandchildren (x)
   (mapcan #'(lambda (c)
                (copy-list (children c)))
           (children x)))

```

这个函数调用 `copy-list` 时存在一个假设 —— `chlidren` 函数返回的是一个已经保存在某个地方的列表，而不是构建了一个新的列表。

一个 `mapcan` 的无损变体可以这样定义：

```
(defun mappend (fn &rest lsts )
    (apply #'append (apply #'mapcar fn lsts)))

```

如果使用 `mappend` 函数，那么 `grandchildren` 的定义就可以省去 `copy-list` ：

```
(defun grandchildren (x)
   (mappend #'children (children x)))
```



## 12.5 示例：二叉搜索树 (Example: Binary Search Trees)











