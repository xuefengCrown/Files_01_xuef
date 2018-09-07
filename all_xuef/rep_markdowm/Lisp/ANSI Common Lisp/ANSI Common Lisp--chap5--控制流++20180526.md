# 控制流

本章的操作符都有一个共同点，就是它们都违反了求值规则。这些操作符让你决定在程序当中何时要求值。如果普通的函数调用是 Lisp 程序的树叶的话，那这些操作符就是连结树叶的树枝。

## 5.1 区块 (Blocks)

Common Lisp 有三个构造区块（block）的基本操作符： `progn` 、 `block` 以及 `tagbody` 。我们已经看过 `progn` 了。在 `progn` 主体中的表达式会依序求值，并返回最后一个表达式的值：

```
> (progn
    (format t "a")
    (format t "b")
    (+ 11 12))
ab
23
```

由于只返回最后一个表达式的值，代表着使用 `progn` （或任何区块）涵盖了副作用。



## 5.2 语境 (Context)

另一个我们用来区分表达式的操作符是 `let` 。它接受一个代码主体，但允许我们在主体内设置新变量：

```
> (let ((x 7)
        (y 2))
    (format t "Number")
    (+ x y))
Number
9

```

一个像是 `let` 的操作符，创造出一个新的词法语境（lexical context）。在这个语境里有两个新变量，然而在外部语境的变量也因此变得不可视了。

前述的 `let` 表达式，实际上等同于：

```
((lambda (x y)
   (format t "Number")
   (+ x y))
 7
 2)
```

这个模型清楚的告诉我们，由 `let` 创造的变量的值，不能依赖其它由同一个 `let` 所创造的变量。举例来说，如果我们试着：

```
(let ((x 2)
      (y (+ x 1)))
  (+ x y))

```

在 `(+ x 1)` 中的 `x` 不是前一行所设置的值，因为整个表达式等同于：

```
((lambda (x y) (+ x y)) 2
                        (+ x 1))

```

这里明显看到 `(+ x 1)` 作为实参传给函数，不能引用函数内的形参 `x` 。

所以如果你真的想要新变量的值，依赖同一个表达式所设立的另一个变量？在这个情况下，使用一个变形版本 `let*` ：

```
> (let* ((x 1)
         (y (+ x 1)))
    (+ x y))
3

```

一个 `let*` 功能上等同于一系列嵌套的 `let` 。这个特别的例子等同于：

```
(let ((x 1))
  (let ((y (+ x 1)))
    (+ x y)))
```

`destructuring-bind` 宏是通用化的 `let` 。其接受单一变量，一个模式 (pattern) ── 一个或多个变量所构成的树 ── 并将它们与某个实际的树所对应的部份做绑定。举例来说：

```
> (destructuring-bind (w (x y) . z) '(a (b c) d e)
    (list w x y z))
(A B C (D E))

```

若给定的树（第二个实参）没有与模式匹配（第一个参数）时，会产生错误。



## 5.3 条件 (Conditionals)

第二简单的条件式是 `when` ，它接受一个测试表达式（test expression）与一个代码主体。若测试表达式求值返回真时，则对主体求值。所以

```
(when (oddp that)
  (format t "Hmm, that's odd.")
  (+ that 1))

```

等同于

```
(if (oddp that)
    (progn
      (format t "Hmm, that's odd.")
      (+ that 1)))

```

`when` 的相反是 `unless` ；它接受相同的实参，但仅在测试表达式返回假时，才对主体求值。



所有条件式的母体 (从正反两面看) 是 `cond` ， `cond` 有两个新的优点：允许多个条件判断，与每个条件相关的代码隐含在 `progn` 里。 `cond` 预期在我们需要使用嵌套 `if` 的情况下使用。 举例来说，这个伪 member 函数

```
(defun our-member (obj lst)
  (if (atom lst)
      nil
      (if (eql (car lst) obj)
          lst
          (our-member obj (cdr lst)))))

```

也可以定义成：

```
(defun our-member (obj lst)
  (cond ((atom lst) nil)
        ((eql (car lst) obj) lst)
        (t (our-member obj (cdr lst)))))

```

事实上，Common Lisp 实现大概会把 `cond` 翻译成 `if` 的形式。

当 `cond` 表达式被求值时，测试条件式依序求值，直到某个测试条件式返回真才停止。当返回真时，与其相关联的表达式会被依序求值，而最后一个返回的数值，会作为 `cond` 的返回值。



当你想要把一个数值与一系列的常量比较时，有 `case` 可以用。我们可以使用 `case` 来定义一个函数，返回每个月份中的天数：

```
(defun month-length (mon)
  (case mon
    ((jan mar may jul aug oct dec) 31)
    ((apr jun sept nov) 30)
    (feb (if (leap-year) 29 28))
    (otherwise "unknown month")))

```

一个 `case` 表达式由一个实参开始，此实参会被拿来与每个子句的键值做比较。接着是零个或多个子句，每个子句由一个或一串键值开始，跟随着零个或多个表达式。键值被视为常量；它们不会被求值。第一个参数的值被拿来与子句中的键值做比较 (使用 `eql` )。如果匹配时，子句剩余的表达式会被求值，并将最后一个求值作为 `case` 的返回值。



## 5.4 迭代 (Iteration)

我们现在知道是可以在 `do` 主体内使用 `return` 、 `return-from` 以及 `go` 。

2.13 节提到 `do` 的第一个参数必须是说明变量规格的列表，列表可以是如下形式：

```
(variable  initial  update)

```

`initial` 与 `update` 形式是选择性的。若 `update` 形式忽略时，每次迭代时不会更新变量。若 `initial` 形式也忽略时，变量会使用 `nil`来初始化。

在 23 页的例子中（译注: 2.13 节），

```
(defun show-squares (start end)
  (do ((i start (+ i 1)))
      ((> i end) 'done)
    (format t "~A ~A~%" i (* i i))))
```



```
> (let ((x 'a))
    (do ((x 1 (+ x 1))
         (y x x))
        ((> x 5))
      (format t "(~A ~A)  " x y)))
(1 A)  (2 1)  (3 2)  (4 3)  (5 4)
NIL

```

每一次迭代时， `x` 获得先前的值，加上一； `y` 也获得 `x` 的前一次数值。

有着同样的精神的是 `dotimes` ，给定某个 `n` ，将会从整数 `0` ，迭代至 `n-1` :

```
(dotimes (x 5 x)
  (format t "~A " x))
0 1 2 3 4
5
```

`dolist` 与 `dotimes 初始列表的第三个表达式皆可省略，省略时为 ``nil` 。注意该表达式可引用到迭代过程中的变量。

（译注：第三个表达式即上例之 `x` ，可以省略，省略时 `dotimes` 表达式的返回值为 `nil` 。）

---

do 的重点 (THE POINT OF do)

在 “The Evolution of Lisp” 里，Steele 与 Garbriel 陈述了 do 的重点， 表达的实在太好了，值得整个在这里引用过来：

撇开争论语法不谈，有件事要说明的是，在任何一个编程语言中，一个循环若一次只能更新一个变量是毫无用处的。 几乎在任何情况下，会有一个变量用来产生下个值，而另一个变量用来累积结果。如果循环语法只能产生变量， 那么累积结果就得借由赋值语句来“手动”实现…或有其他的副作用。具有多变量的 do 循环，体现了产生与累积的本质对称性，允许可以无副作用地表达迭代过程：

```
(defun factorial (n)
  (do ((j n (- j 1))
       (f 1 (* j f)))
    ((= j 0) f)))

```

当然在 step 形式里实现所有的实际工作，一个没有主体的 do 循环形式是较不寻常的。

---

函数 `mapc` 和 `mapcar` 很像，但不会 `cons` 一个新列表作为返回值，所以使用的唯一理由是为了副作用。它们比 `dolist` 来得灵活，因为可以同时遍历多个列表：

```
> (mapc #'(lambda (x y)
          (format t "~A ~A  " x y))
      '(hip flip slip)
      '(hop flop slop))
HIP HOP  FLIP FLOP  SLIP SLOP
(HIP FLIP SLIP)

```

总是返回 `mapc` 的第二个参数。

## 5.5 多值 (Multiple Values)

多值允许一个函数返回多件事情的计算结果，而不用构造一个特定的结构。举例来说，内置的 `get-decoded-time` 返回 9 个数值来表示现在的时间：秒，分，时，日期，月，年，天，以及另外两个数值。

多值也使得查询函数可以分辨出 `nil` 与查询失败的情况。这也是为什么 `gethash` 返回两个值。因为它使用第二个数值来指出成功还是失败，我们可以在哈希表里储存 `nil` ，就像我们可以储存别的数值那样。

`values` 函数返回多个数值。它一个不少地返回你作为数值所传入的实参：

```
> (values 'a nil (+ 2 4))
A
NIL
6

```

如果一个 `values` 表达式，是函数主体最后求值的表达式，它所返回的数值变成函数的返回值。多值可以原封不地通过任何数量的返回来传递：

```
> ((lambda () ((lambda () (values 1 2)))))
1
2

```

然而若只预期一个返回值时，第一个之外的值会被舍弃：

```
> (let ((x (values 1 2)))
    x)
1

```

通过不带实参使用 `values` ，是可能不返回值的。在这个情况下，预期一个返回值的话，会获得 `nil` :

```
> (values)
> (let ((x (values)))
    x)
NIL

```

要接收多个数值，我们使用 `multiple-value-bind` :

```
> (multiple-value-bind (x y z) (values 1 2 3)
    (list x y z))
(1 2 3)

> (multiple-value-bind (x y z) (values 1 2)
    (list x y z))
(1 2 NIL)

```

如果变量的数量大于数值的数量，剩余的变量会是 `nil` 。如果数值的数量大于变量的数量，多余的值会被舍弃。所以只想印出时间我们可以这么写:

```
> (multiple-value-bind (s m h) (get-decoded-time)
    (format t "~A:~A:~A" h m s))
"4:32:13"
```

## 5.6 中止 (Aborts)

你可以使用 `return` 在任何时候离开一个 `block` 。有时候我们想要做更极端的事，在数个函数调用里将控制权转移回来。要达成这件事，我们使用 `catch` 与 `throw` 。一个 `catch` 表达式接受一个标签（tag），标签可以是任何类型的对象，伴随着一个表达式主体：

```
(defun super ()
  (catch 'abort
    (sub)
    (format t "We'll never see this.")))

(defun sub ()
  (throw 'abort 99))

```

表达式依序求值，就像它们是在 `progn` 里一样。在这段代码里的任何地方，一个带有特定标签的 `throw` 会导致 `catch` 表达式直接返回：

```
> (super)
99

```

一个带有给定标签的 `throw` ，为了要到达匹配标签的 `catch` ，会将控制权转移 (因此杀掉进程)给任何有标签的 `catch` 。如果没有一个 `catch` 符合欲匹配的标签时， `throw` 会产生一个错误。

调用 `error` 同时中断了执行，本来会将控制权转移到调用树（calling tree）的更高点，取而代之的是，它将控制权转移给 Lisp 错误处理器（error handler）。通常会导致调用一个中断循环（break loop）。以下是一个假定的 Common Lisp 实现可能会发生的事情：

```
> (progn
    (error "Oops!")
    (format t "After the error."))
Error: Oops!
       Options: :abort, :backtrace
>>

```

译注：2 个 `>>` 显示进入中断循环了。

关于错误与状态的更多讯息，参见 14.6 小节以及附录 A。

有时候你想要防止代码被 `throw` 与 `error` 打断。借由使用 `unwind-protect` ，可以确保像是前述的中断，不会让你的程序停在不一致的状态。一个 `unwind-protect` 接受任何数量的实参，并返回第一个实参的值。然而即便是第一个实参的求值被打断时，剩下的表达式仍会被求值：

```
> (setf x 1)
1
> (catch 'abort
    (unwind-protect
      (throw 'abort 99)
      (setf x 2)))
99
> x
2

```

在这里，即便 `throw` 将控制权交回监测的 `catch` ， `unwind-protect` 确保控制权移交时，第二个表达式有被求值。无论何时，一个确切的动作要伴随着某种清理或重置时， `unwind-protect` 可能会派上用场。在 121 页提到了一个例子。









