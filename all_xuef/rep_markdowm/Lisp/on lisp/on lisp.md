

# chap2

## 映射类函数

很多内置的 Common Lisp 函数都可以把函数作为参数。这些内置函数中，最常用的是映射类的函数。例
如 mapcar 带有两个以上参数 一个函数加上一个以上的列表 (每个列表都分别是函数的参数)，然后它
可以将参数里的函数依次作用在每个列表的元素上：

```lisp
> (mapcar #’(lambda (x) (+ x 10))
		  ’(1 2 3))
(11 12 13)
> (mapcar #’+
          ’(1 2 3)
          ’(10 100 1000))
(11 102 1003)
```

## sort

```lisp
> (sort ’(1 4 2 5 6 7 3) #’<)
(1 2 3 4 5 6 7)
```

## remove-if

```lisp
> (remove-if #’evenp ’(1 2 3 4 5 6 7))
(1 3 5 7)
```

## rules

但无论是使用内置的工具，比如sort，还是编写你的实用工具，基本原则是一样的：与其把功能写死，不如传进去一个函数参数。

## 2.4 作为属性的函数

函数作为 Lisp 对象这一事实也创造了条件，让我们能够编写出那种可以随时扩展以满足新需求的程序。
假设我们需要写一个以动物种类作为参数并产生相应行为的函数。

在大多数语言中，会使用 case 语句达到这个目的，Lisp 里也可以用同样的办法：

```lisp
(defun behave (animal)
	(case animal
      (dog (wag-tail)
      	   (bark))
      (rat (scurry)
      	   (squeak))
      (cat (rub-legs)
		   (scratch-carpet))))
```

如果要增加一种新动物该怎么办呢？如果计划增加新的动物，那么把 behave 定义成下面的样子可能会更
好一些：

```lisp
(defun behave (animal)
	(funcall (get animal ’behavior)))
```

同时把每种个体动物的行为以单独的函数形式保存，例如，存放在以它们名字命名的属性列表里：

```lisp
(setf (get 'dog 'behavior)
  #’(lambda ()
      (wag-tail)
      (bark)))
```

用这种方式处理的话，要增加一种新动物，所有你需要做的事情就是定义一个新的属性。一个函数都不用
重写。
上述第二种方法尽管更灵活，但看上去要慢些。实际上也是如此。如果速度很关键，我们可以把属性表换
成结构体，而且特别要用编译过的函数代替解释性的函数。

这样使用函数相当于面向对象编程中的方法概念。总的来说，方法是作为对象属性的一种函数，这也正是
我们手里有的。如果把继承引入这个模型，你就得到了面向对象编程的全部要素。第 25 章将用少得惊人
的代码来说明这一点。
面向对象编程的一大亮点是它能让程序可扩展。这一点在 Lisp 界激起的反响要小很多，因为在这里，人们
早已把可扩展性当成理所当然的事情了。如果我们要的可扩展性不是很依赖继承，那么纯 Lisp 可能就已
经足够应付了。

## 2.5 作用域（CL默认词法作用域）

```lisp
(let ((y 7))
  (defun scope-test (x)
  	(list x y)))
```

在函数表达式里，x 是受约束的，而 y 是自由的。自由变量有意思的地方就在于，这种变量应有的值并不那
么显而易见。一个约束变量的值是确信无疑的 当调用 scope-test 时，x 的值就是通过参数传给它的
值。但 y 的值应该是什么呢？这要看具体方言的作用域规则。
在动态作用域的 Lisp 里，要想找出当 scope-test 执行时自由变量的值，我们要往回逐个检查函数的调用
链。当发现 y 被绑定时，这个被绑定的值即被用在 scope-test 中。如果没有发现，那就取 y 的全局值。这
样，在用动态作用域的 Lisp 里，在调用的时候 y 将会产生这样的值：

```lisp
> (let ((y 5))
	(scope-test 3))
(3 5)
```

在词法作用域的 Lisp 里，我们不再往回逐个检查函数的调用链，而是逐层检查定义这个函数时，它所处的
各层外部环境。在一个词法作用域 Lisp 里，我们的示例将捕捉到定义 scope-test 时，变量 y 的绑定。所
以可以在 Common Lisp 里观察到下面的现象：

```lisp
> (let ((y 5))
	(scope-test 3))
(3 7)
```

这里将 y 绑定到 5。这样做对函数调用的返回值不会有丝毫影响。
尽管你仍然可以通过将变量声明为 special 来得到动态作用域，但是词法作用域是 Common Lisp 的默认行
为。总的来说，Lisp 社区对昨日黄花的动态作用域几乎没什么留恋。因为它经常会导致痛苦而又难以捉摸
的 bug。而词法作用域不仅仅是一种避免错误的手段。在下一章我们会看到，它同时也带来了一些崭新的
编程技术。

## 2.6 闭包

由于 Common Lisp 是词法作用域的，所以如果定义含有自由变量的函数，系统就必须在函数定义时保存那
些变量的绑定。这种函数和一组变量绑定的组合称为闭包。我们发现，闭包在各种场合都能大显身手。

```lisp
(defun list+ (lst n)
	(mapcar #’(lambda (x) (+ x n))
		lst))
```

闭包在 Abelson 和 Sussman 的经典教材《计算机程序的构造和解释》一书中扮演了更加重要的角色。

闭包是带有局部状态的函数。使用这种状态最简单的方式是如下的情况：

```lisp
(let ((counter 0))
	(defun new-id () (incf counter))
	(defun reset-id () (setq counter 0)))
```

这两个函数共享一个计数器变量。前者返回计数器的下一个值，后者把计数器重置到 0。这种方式避免了
对计数器变量非预期的引用，尽管同样的功能也可以用一个全局的计数器变量完成。
如果返回的函数能带有局部状态，那么也会很有帮助。例如这个 make-adder 函数：

```lisp
(defun make-adder (n)
	#’(lambda (x) (+ x n)))
```

甚至有可能返回共享同一数据对象的一组闭包。图 2.1 中的函数被用来创建原始数据库。它接受一个关
联表 (db)，并相应返回一个由查询、追加和删除这三个闭包所组成的列表。

```lisp
(defun make-dbms (db)
  (list
    #’(lambda (key)
    	(cdr (assoc key db)))
    #’(lambda (key val)
        (push (cons key val) db)
        	key)
    #’(lambda (key)
    	(setf db (delete key db :key #’car))
      		key)))
```

每次调用 make-dbms 都会创建新的数据库 这个新数据库就是一组新函数，它们把自己的共享拷贝封
存在一张关联表 (assoc-list) 里面。

```lisp
> (setq cities (make-dbms ’((boston . us) (paris .france))))
(#<Interpreted-Function 8022E7>
#<Interpreted-Function 802317>
#<Interpreted-Function 802347>)
```

数据库里实际的关联表是对外界不可见的，我们甚至不知道它是个关联表——但是可以通过构成 cities
的那些函数访问到它：

```lisp
> (funcall (car cities) ’boston)
US
> (funcall (second cities) ’london ’england)
LONDON
> (funcall (car cities) ’london)
ENGLAND
```

调用列表的 car 多少有些难看。实际的程序中，函数访问的入口可能隐藏在结构体里。当然也可以设法更
简洁地使用它们 数据库可以通过这样的函数间接访问：

```lisp
(defun lookup (key db)
	(funcall (car db) key))
```

无论怎样，这种改进都不会影响到闭包的基本行为。
实际程序中的闭包和数据结构往往比我们在 make-adder 和 make-dbms 里看到的更加精巧。这里用到的
单个共享变量也可以发展成任意数量的变量，每个都可以约束到任意的数据结构上。
闭包是 Lisp 的众多独特和实实在在的优势之一。如果下些工夫的话，还可能把有的 Lisp 程序翻译成能力
稍弱的语言，但只要试着去翻译上面那些使用了闭包的程序，你就会明白这种抽象帮我们省去了多少工作。
后续章节将进一步探讨闭包的更多细节。第 5 章展示了如何用它们构造复合函数，接着在第 6 章里会继续
介绍如何用它们替代传统的数据结构。

## 2.7 局部函数

尽管如此，在 let 与 labels 之间有一个重要的区别。在 let 表达式里，变量的值不能依赖于同一个 let 里
生成的另一个变量 就是说，你不能说

```lisp
(let ((x 10) (y x))
	y)
```

然后认为这个新的 y 能反映出那个新 x 的值。相反，在 labels 里定义的函数 f 的函数体里就可以引用那
里定义的其他函数，包括 f 本身，这就使定义递归函数成为可能。

## 2.8 尾递归

递归函数自己调用自己。如果函数调用自己之后不做其他工作，这种调用就称为 尾递归 (tail-recursive)。
下面这个函数不是尾递归的

```lisp
(defun our-length (lst)
  (if (null lst)
      0
      (1+ (out-length (cdr lst)))))
```

因为在从递归调用返回之后，我们又把结果传给了 1+。而下面这个函数就是尾递归的

```lisp
(defun our-find-if (fn lst)
  (if (funcall fn (car lst))
      (car lst)
      (our-find-if fn (cdr lst))))
```

如果一个函数不是尾递归的话，常常可以把一个使用累积器 (accumulator) 的局部函数嵌入到其中，用这种
方法把它转换成尾递归的形式。在这里，累积器指的是一个参数，它代表着到目前为止计算得到的值。例
如 our-length 可以转换成

```lisp
(defun our-length (lst)
	(labels ((rec (lst acc)
		(if (null lst)
            acc
			(rec (cdr lst) (1+ acc)))))
	(rec lst 0)))
```

## 2.9 编译















































