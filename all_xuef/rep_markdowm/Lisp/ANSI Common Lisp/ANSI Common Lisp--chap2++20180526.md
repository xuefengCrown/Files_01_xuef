# ANSI Common Lisp

## chap1 intro

在 Lisp 里，我们用单一的表示法，来表达所有的概念。

 ### 2.2 求值

Lisp 提供 `quote` 作为一种*保护*表达式不被求值的方式。下一节将解释为什么这种保护很有用。



### 2.3 数据 data

```lisp
Integer 256
String "hello"

符号 Symbol 
> 'Artichoke
ARTICHOKE
列表 List
> '(the list (a b c) has 3 elements)


```

我们现在来到领悟 Lisp 最卓越特性的地方之一。Lisp的程序是用列表来表示的。如果实参的优雅与弹性不能说服你 Lisp 表示法是无价的工具，这里应该能使你信服。这代表着 Lisp 程序可以写出 Lisp 代码。 Lisp 程序员可以（并且经常）写出能为自己写程序的程序。

```lisp
> (list '(+ 2 1) (+ 2 1))
((+ 2 1) 3)
```



### 2.4 List Operations

```lisp
cons
car
cdr
first
rest
```



### 2.5 真与假

```lisp
> (listp '(a b c))
T

> (null nil)
T

> (atom ())
T

> (atom '(1 2))

> (not nil)
T
```

```lisp
> (if (listp '(a b c))
      (+ 1 2)
      (+ 5 6))
3
```

与 `quote` 相同， `if` 是特殊的操作符。不能用函数来实现，因为实参在函数调用时永远会被求值，而 `if` 的特点是，只有最后两个实参的其中一个会被求值。



逻辑操作符 `and` 和 `or` 与条件式类似。两者都接受任意数量的实参，但仅对能影响返回值的几个实参求值。如果所有的实参都为 `真` （即非 `nil` ），那么 `and` 会返回最后一个实参的值：

```lisp
> (and t (+ 1 2))
3
```

如果其中一个实参为 `假` ，那之后的所有实参都不会被求值。 `or` 也是如此，只要碰到一个为 `真` 的实参，就停止对之后所有的实参求值。

以上这两个操作符称为*宏*。宏和特殊的操作符一样，可以绕过一般的求值规则。



### 2.6 Functions

```lisp
> (defun our-third (x)
   (car (cdr (cdr x))))
OUR-THIRD
```



### 2.7 Recursion

函数可以调用任何函数，包括自己。自己调用自己的函数是*递归*的。 Common Lisp 函数 `member` ，测试某个东西是否为列表的成员。下面是定义成递归函数的简化版：

```lisp
> (defun our-member (obj lst)
   (if (null lst)
       nil
   (if (eql (car lst) obj)
       lst
       (our-member obj (cdr lst)))))
OUR-MEMBER

```

下面是 `our-member` 的定义对应到英语的描述。为了知道一个对象 `obj` 是否为列表 `lst` 的成员，我们

> 1. 首先检查 `lst` 列表是否为空列表。如果是空列表，那 `obj` 一定不是它的成员，结束。
> 2. 否则，若 `obj` 是列表的第一个元素时，则它是列表的成员。
> 3. 不然只有当 `obj` 是列表其余部分的元素时，它才是列表的成员。

当你想要了解递归函数是怎么工作时，把它翻成这样的叙述有助于你理解。



### 2.9 Input and Output

最普遍的 Common Lisp 输出函数是 `format` 。接受两个或两个以上的实参，第一个实参决定输出要打印到哪里，第二个实参是字符串模版，而剩余的实参，通常是要插入到字符串模版，用打印表示法（printed representation）所表示的对象。下面是一个典型的例子：

```lisp
> (format t "~A plus ~A equals ~A. ~%" 2 3 (+ 2 3))
2 plus 3 equals 5.
NIL
```

注意到有两个东西被打印出来。第一行是 `format` 印出来的。第二行是调用 `format` 函数的返回值，就像平常顶层会打印出来的一样。通常像 `format` 这种函数不会直接在顶层调用，而是在程序内部里使用，所以返回值不会被看到。

`format` 的第一个实参 `t` ，表示输出被送到缺省的地方去。通常是顶层。第二个实参是一个用作输出模版的字符串。在这字符串里，每一个 `~A` 表示了被填入的位置，而 `~%` 表示一个换行。这些被填入的位置依序由后面的实参填入。



标准的输入函数是 `read` 。当没有实参时，会读取缺省的位置，通常是顶层。下面这个函数，提示使用者输入，并返回任何输入的东西：

```lisp
(defun askem (string)
 (format t "~A" string)
 (read))
它的行为如下：

> (askem "How old are you?")
How old are you?29

29
```

记住 `read` 会一直永远等在这里，直到你输入了某些东西，并且（通常要）按下回车。

第二件关于 `read` 所需要知道的事是，它很强大： `read` 是一个完整的 Lisp 解析器（parser）。不仅是可以读入字符，然后当作字符串返回它们。它解析它所读入的东西，并返回产生出来的 Lisp 对象。在上述的例子，它返回一个数字。

`askem` 的定义虽然很短，但体现出一些我们在之前的函数没看过的东西。函数主体可以有不只一个表达式。函数主体可以有任意数量的表达式。当函数被调用时，会依序求值，函数会返回最后一个的值。

在之前的每一节中，我们坚持所谓“纯粹的” Lisp ── 即没有副作用的 Lisp 。副作用是指，表达式被求值后，对外部世界的状态做了某些改变。当我们对一个如 `(+ 1 2)` 这样纯粹的 Lisp 表达式求值时，没有产生副作用。它只返回一个值。但当我们调用 `format` 时，它不仅返回值，还印出了某些东西。这就是一种副作用。

当我们想要写没有副作用的程序时，则定义多个表达式的函数主体就没有意义了。最后一个表达式的值，会被当成函数的返回值，而之前表达式的值都被舍弃了。如果这些表达式没有副作用，你没有任何理由告诉 Lisp ，为什么要去对它们求值。



### 2.10 Variables

`let` 是一个最常用的 Common Lisp 的操作符之一，它让你引入新的局部变量（local variable）：

```lisp
> (let ((x 1) (y 2))
     (+ x y))
3
```

这些变量只在 `let` 的函数体内有效。

```lisp
(defun ask-number ()
 (format t "Please enter a number. ")
 (let ((val (read)))
   (if (numberp val)
       val
       (ask-number))))

> (ask-number)
Please enter a number. a
Please enter a number. (ho hum)
Please enter a number. 52
52
```



我们已经看过的这些变量都叫做局部变量。它们只在特定的上下文里有效。另外还有一种变量叫做全局变量（global variable），是在任何地方都是可视的。



#### global variable

```lisp
> (defparameter *glob* 99)
*GLOB*
```



#### global cons

```lisp
(defconstant limit (+ *glob* 1))
```

### 2.11 赋值 (Assignment)

```lisp
> (setf *glob* 98)
98
> (let ((n 10))
   (setf n 2)
   n)
2
```

如果 `setf` 的第一个实参是符号（symbol），且符号不是某个局部变量的名字，则 `setf` 把这个符号设为全局变量：

```lisp
> (setf x (list 'a 'b 'c))
(A B C)
```

你不仅可以给变量赋值。传入 `setf` 的第一个实参，还可以是表达式或变量名。在这种情况下，第二个实参的值被插入至第一个实参所引用的位置：

```lisp
> (setf (car x) 'n)
N
> x
(N B C)
```



```lisp
(setf a 'b
      c 'd
      e 'f)
```



### 2.12 Functional Programming

函数式编程意味着撰写利用返回值而工作的程序，而不是修改东西。它是 Lisp 的主流范式。大部分 Lisp 的内置函数被调用是为了取得返回值，而不是副作用。

举例来说，函数 `remove` 接受一个对象和一个列表，返回不含这个对象的新列表：

```lisp
> (setf lst '(c a r a t))
(C A R A T)
> (remove 'a lst)
(C R T)
```

为什么不干脆说 `remove` 从列表里移除一个对象？因为它不是这么做的。原来的表没有被改变：

```lisp
> lst
(C A R A T)
```

若你真的想从列表里移除某些东西怎么办？在 Lisp 通常你这么做，把这个列表当作实参，传入某个函数，并使用 `setf` 来处理返回值。要移除所有在列表 `x` 的 `a` ，我们可以说：

```lisp
(setf x (remove 'a x))
```

函数式编程本质上意味着避免使用如 `setf` 的函数。起初可能觉得这根本不可能，更遑论去做了。怎么可以只凭返回值来建立程序？

完全不用到副作用是很不方便的。然而，随着你进一步阅读，会惊讶地发现需要用到副作用的地方很少。副作用用得越少，你就更上一层楼。

函数式编程最重要的优点之一是，它允许交互式测试（interactive testing）。在纯函数式的程序里，你可以测试每个你写的函数。如果它返回你预期的值，你可以有信心它是对的。这额外的信心，集结起来，会产生巨大的差别。当你改动了程序里的任何一个地方，会得到即时的改变。而这种即时的改变，使我们有一种新的编程风格。类比于电话与信件，让我们有一种新的通讯方式。



### 2.13 迭代 (Iteration)

当我们想重复做一些事情时，迭代比递归来得更自然。典型的例子是用迭代来产生某种表格。这个函数

```lisp
(defun show-squares (start end)
  (do ((i start (+ i 1)))
      ((> i end) 'done)
    (format t "~A ~A~%" i (* i i))))
```

作为对比，以下是递归版本的 `show-squares` ：

```lisp
(defun show-squares (i end)
   (if (> i end)
     'done
     (progn
       (format t "~A ~A~%" i (* i i))
       (show-squares (+ i 1) end))))
```

唯一的新东西是 `progn` 。 `progn` 接受任意数量的表达式，依序求值，并返回最后一个表达式的值。



为了处理某些特殊情况， Common Lisp 有更简单的迭代操作符。举例来说，要遍历列表的元素，你可能会使用 `dolist` 。以下函数返回列表的长度：

```lisp
(defun our-length (lst)
  (let ((len 0))
    (dolist (obj lst)
      (setf len (+ len 1)))
    len))
```

这里 `dolist` 接受这样形式的实参*(variable expression)*，跟着一个具有表达式的函数主体。函数主体会被求值，而变量相继与表达式所返回的列表元素绑定。因此上面的循环说，对于列表 `lst` 里的每一个 `obj` ，递增 `len` 。很显然这个函数的递归版本是：

```lisp
(defun our-length (lst)
 (if (null lst)
     0
     (+ (our-length (cdr lst)) 1)))
```

也就是说，如果列表是空表，则长度为 `0` ；否则长度就是对列表取 `cdr` 的长度加一。递归版本的 `our-length` 比较易懂，但由于它不是尾递归（tail-recursive）的形式 (见 13.2 节)，效率不是那么高。



### 2.14 函数作为对象 (Functions as Objects)

函数在 Lisp 里，和符号、字符串或列表一样，是稀松平常的对象。

```lisp
(function +)

> #'+
#<Compiled-Function + 17BA4E>
```

和别种对象类似，可以把函数当作实参传入。有个接受函数作为实参的函数是 `apply` 。`apply` 接受一个函数和实参列表，并返回把传入函数应用在实参列表的结果：

```lisp
> (apply #'+ '(1 2 3))
6
```

`apply` 可以接受任意数量的实参，只要最后一个实参是列表即可：

```lisp
> (apply #'+ 1 2 '(3 4 5))
15
```

函数 `funcall` 做的是一样的事情，但不需要把实参包装成列表。

```lisp
> (funcall #'+ 1 2 3)
6
```



要直接引用一个函数，我们使用所谓的*lambda 表达式*。一个 `lambda` 表达式是一个列表，列表包含符号 `lambda` ，接着是形参列表，以及由零个或多个表达式所组成的函数体。

下面的 `lambda` 表达式，表示一个接受两个数字并返回两者之和的函数：

```lisp
(lambda (x y)
 (+ x y))
```

```lisp
> ((lambda (x) (+ x 100)) 1)
101
```

而通过在 `lambda` 表达式前面贴上 `#'` ，我们得到对应的函数，

```lisp
> (funcall #'(lambda (x) (+ x 100))
          1)
```

### 2.15 类型 (Types)

Lisp 处理类型的方法非常灵活。在很多语言里，变量是有类型的，得声明变量的类型才能使用它。在 Common Lisp 里，数值才有类型，而变量没有。你可以想像每个对象，都贴有一个标明其类型的标签。这种方法叫做*显式类型*（*manifest typing*）。你不需要声明变量的类型，因为变量可以存放任何类型的对象。

Common Lisp 的内置类型，组成了一个类别的层级。对象总是不止属于一个类型。举例来说，数字 27 的类型，依普遍性的增加排序，依序是 `fixnum` 、 `integer` 、 `rational` 、 `real` 、 `number` 、 `atom` 和 `t` 类型。（数值类型将在第 9 章讨论。）类型 `t` 是所有类型的基类（supertype）。所以每个对象都属于 `t` 类型。

函数 `typep` 接受一个对象和一个类型，然后判定对象是否为该类型，是的话就返回真：

```lisp
> (typep 27 'integer)
T
```



### 2.16 展望 (Looking Forward)

```commonlisp
本章仅谈到 Lisp 的表面。然而，一种非比寻常的语言形象开始出现了。首先，这个语言用单一的语法，来表达所有的程序结构。语法基于列表，列表是一种 Lisp 对象。函数本身也是 Lisp 对象，函数能用列表来表示。而 Lisp 本身就是 Lisp 程序。几乎所有你定义的函数，与内置的 Lisp 函数没有任何区别。

如果你对这些概念还不太了解，不用担心。 Lisp 介绍了这么多新颖的概念，在你能驾驭它们之前，得花时间去熟悉它们。不过至少要了解一件事：在这些概念当中，有着优雅到令人吃惊的概念。

Richard Gabriel 曾经半开玩笑的说， C 是拿来写 Unix 的语言。我们也可以说， Lisp 是拿来写 Lisp 的语言。但这是两种不同的论述。一个可以用自己编写的语言和一种适合编写某些特定类型应用的语言，是有着本质上的不同。这开创了新的编程方法：你不但在语言之中编程，还把语言改善成适合程序的语言。如果你想了解 Lisp 编程的本质，理解这个概念是个好的开始。
```









































































































