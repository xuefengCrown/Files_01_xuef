Common Lisp 对象系统，或称 CLOS，是一组用来实现面向对象编程的操作集。由于它们有着同样的历史，通常将这些操作视为一个群组。 [λ](http://acl.readthedocs.org/en/latest/zhCN/notes-cn.html#notes-176) 技术上来说，它们与其他部分的 Common Lisp 没什么大不同： `defmethod` 和 `defun` 一样，都是整合在语言中的一个部分。



## 11.1 面向对象编程

面向对象编程意味着程序组织方式的改变。这个改变跟已经发生过的处理器运算处理能力分配的变化雷同。在 1970 年代，一个多用户的计算机系统代表着，一个或两个大型机连接到大量的[哑终端](http://zh.wikipedia.org/wiki/%E5%93%91%E7%BB%88%E7%AB%AF)(dumb terminal)。现在更可能的是大量相互通过网络连接的工作站 (workstation)。系统的运算处理能力现在分布至个体用户上，而不是集中在一台大型的计算机上。

面向对象编程所带来的变革与上例非常类似，前者打破了传统程序的组织方式。不再让单一的程序去操作那些数据，而是告诉数据自己该做什么，程序隐含在这些新的数据“对象”的交互过程之中。

举例来说，假设我们要算出一个二维图形的面积。一个办法是写一个单独的函数，让它检查其参数的类型，然后视类型做处理，如图 11.1 所示。

```
(defstruct rectangle
  height width)

(defstruct circle
  radius)

(defun area (x)
  (cond ((rectangle-p x)
         (* (rectangle-height x) (rectangle-width x)))
        ((circle-p x)
         (* pi (expt (circle-radius x) 2)))))

> (let ((r (make-rectangle)))
    (setf (rectangle-height r) 2
          (rectangle-width r) 3)
    (area r))
6

```

**图 11.1: 使用结构及函数来计算面积**

使用 CLOS 我们可以写出一个等效的程序，如图 11.2 所示。在面向对象模型里，我们的程序被拆成数个独一无二的方法，每个方法为某些特定类型的参数而生。图 11.2 中的两个方法，隐性地定义了一个与图 11.1 相似作用的 `area` 函数，当我们调用 `area` 时，Lisp 检查参数的类型，并调用相对应的方法。

```
(defclass rectangle ()
  (height width))

(defclass circle ()
  (radius))

(defmethod area ((x rectangle))
  (* (slot-value x 'height) (slot-value x 'width)))

(defmethod area ((x circle))
  (* pi (expt (slot-value x 'radius) 2)))

> (let ((r (make-instance 'rectangle)))
    (setf (slot-value r 'height) 2
          (slot-value r 'width) 3)
    (area r))
6

```

**图 11.2: 使用类型与方法来计算面积**

通过这种方式，我们将函数拆成独一无二的方法，面向对象暗指*继承* (*inheritance*) ── 槽（slot）与方法（method）皆有继承。在图 11.2 中，作为第二个参数传给 `defclass` 的空列表列出了所有基类。假设我们要定义一个新类，上色的圆形 (colored-circle)，则上色的圆形有两个基类， `colored` 与 `circle` ：

```
(defclass colored ()
  (color))

(defclass colored-circle (circle colored)
  ())
```

当我们创造 `colored-circle` 类的实例 (instance)时，我们会看到两个继承：

1. `colored-circle` 的实例会有两个槽：从 `circle` 类继承而来的 `radius` 以及从 `colored` 类继承而来的 `color` 。
2. 由于没有特别为 `colored-circle` 定义的 `area` 方法存在，若我们对 `colored-circle` 实例调用 `area` ，我们会获得替 `circle` 类所定义的 `area` 方法。

从实践层面来看，面向对象编程代表着以方法、类、实例以及继承来组织程序。为什么你会想这么组织程序？面向对象方法的主张之一说这样使得程序更容易改动。如果我们想要改变 `ob` 类对象所显示的方式，我们只需要改动 `ob` 类的 `display` 方法。如果我们希望创建一个新的类，大致上与 `ob` 相同，只有某些方面不同，我们可以创建一个 `ob`类的子类。在这个子类里，我们仅改动我们想要的属性，其他所有的属性会从 `ob` 类默认继承得到。要是我们只是想让某个 `ob` 对象和其他的 `ob` 对象不一样，我们可以新建一个 `ob` 对象，直接修改这个对象的属性即可。若是当时的程序写的很讲究，我们甚至不需要看程序中其他的代码一眼，就可以完成种种的改动。



## 11.2 类与实例(Class and Instances)

在 4.6 节时，我们看过了创建结构的两个步骤：我们调用 `defstruct` 来设计一个结构的形式，接着通过一个像是 `make-point` 这样特定的函数来创建结构。创建实例 (instances)同样需要两个类似的步骤。首先我们使用 `defclass` 来定义一个类别 (Class):

```
(defclass circle ()
  (radius center))
```

这个定义说明了 `circle` 类别的实例会有两个槽 (*slot*)，分别名为 `radius` 与 `center` （槽类比于结构里的字段 「field」）。

要创建这个类的实例，我们调用通用的 `make-instance` 函数，而不是调用一个特定的函数，传入的第一个参数为类别名称：

```
> (setf c (make-instance 'circle))
#<CIRCLE #XC27496>
```

要给这个实例的槽赋值，我们可以使用 `setf` 搭配 `slot-value` ：

```
> (setf (slot-value c 'radius) 1)
1
```

与结构的字段类似，未初始化的槽的值是未定义的 (undefined)。



## 11.3 槽的属性 (Slot Properties)

传给 `defclass` 的第三个参数必须是一个槽定义的列表。如上例所示，最简单的槽定义是一个表示其名称的符号。在一般情况下，一个槽定义可以是一个列表，第一个是槽的名称，伴随着一个或多个属性 (property)。属性像关键字参数那样指定。

通过替一个槽定义一个访问器 (accessor)，我们隐式地定义了一个可以引用到槽的函数，使我们不需要再调用 `slot-value` 函数。如果我们如下更新我们的 `circle` 类定义，

```
(defclass circle ()
  ((radius :accessor circle-radius)
   (center :accessor circle-center)))

```

那我们能够分别通过 `circle-radius` 及 `circle-center` 来引用槽：

```
> (setf c (make-instance 'circle))
#<CIRCLE #XC5C726>

> (setf (circle-radius c) 1)
1

> (circle-radius c)
1

```

通过指定一个 `:writer` 或是一个 `:reader` ，而不是 `:accessor` ，我们可以获得访问器的写入或读取行为。

要指定一个槽的缺省值，我们可以给入一个 `:initform` 参数。若我们想要在 `make-instance` 调用期间就将槽初始化，我们可以用 `:initarg` 定义一个参数名。 [[1\]](http://acl.readthedocs.io/en/latest/zhCN/ch11-cn.html#id8) 加入刚刚所说的两件事，现在我们的类定义变成：

```
(defclass circle ()
  ((radius :accessor circle-radius
           :initarg :radius
           :initform 1)
   (center :accessor circle-center
           :initarg :center
           :initform (cons 0 0))))

```

现在当我们创建一个 `circle` 类的实例时，我们可以使用关键字参数 `:initarg` 给槽赋值，或是將槽的值设为 `:initform` 所指定的缺省值。

```
> (setf c (make-instance 'circle :radius 3))
#<CIRCLE #XC2DE0E>
> (circle-radius c)
3
> (circle-center c)
(0 . 0)

```

注意 `initarg` 的优先级比 `initform` 要高。

我们可以指定某些槽是共享的 ── 也就是每个产生出来的实例，共享槽的值都会是一样的。我们通过声明槽拥有 `:allocation :class` 来办到此事。（另一个办法是让一个槽有 `:allocation :instance` ，但由于这是缺省设置，不需要特别再声明一次。）当我们在一个实例中，改变了共享槽的值，则其它实例共享槽也会获得相同的值。所以我们会想要使用共享槽来保存所有实例都有的相同属性。

举例来说，假设我们想要模拟一群成人小报 (a flock of tabloids)的行为。（**译注**：可以看看[什么是 tabloids](http://tinyurl.com/9n4dckk)。）在我们的模拟中，我们想要能够表示一个事实，也就是当一家小报采用一个头条时，其它小报也会跟进的这个行为。我们可以通过让所有的实例共享一个槽来实现。若 `tabloid` 类别像下面这样定义，

```
(defclass tabloid ()
  ((top-story :accessor tabloid-story
              :allocation :class)))

```

那么如果我们创立两家小报，无论一家的头条是什么，另一家的头条也会是一样的：

```
> (setf daily-blab (make-instance 'tabloid)
        unsolicited-mail (make-instance 'tabloid))
#<TABLOID #x302000EFE5BD>
> (setf (tabloid-story daily-blab) 'adultery-of-senator)
ADULTERY-OF-SENATOR
> (tabloid-story unsolicited-mail)
ADULTERY-OF-SENATOR

```

**译注**： ADULTERY-OF-SENATOR 参议员的性丑闻

若有给入 `:documentation` 属性的话，用来作为 `slot` 的文档字符串。通过指定一个 `:type` ，你保证一个槽里只会有这种类型的元素。类型声明会在 13.3 节讲解。



## 11.4 基类 (Superclasses)

`defclass` 接受的第二个参数是一个列出其基类的列表。一个类别继承了所有基类槽的联集。所以要是我们将 `screen-circle` 定义成 `circle` 与 `graphic` 的子类，

```
(defclass graphic ()
  ((color :accessor graphic-color :initarg :color)
   (visible :accessor graphic-visible :initarg :visible
            :initform t)))

(defclass screen-circle (circle graphic) ())

```

则 `screen-circle` 的实例会有四个槽，分别从两个基类继承而来。一个类别不需要自己创建任何新槽； `screen-circle` 的存在，只是为了提供一个可创建同时从 `circle`及 `graphic` 继承的实例。

访问器及 `:initargs` 参数可以用在 `screen-circle` 的实例，就如同它们也可以用在 `circle` 或 `graphic` 类别那般：

```
> (graphic-color (make-instance 'screen-circle
                                :color 'red :radius 3))
RED

```

我们可以使每一个 `screen-circle` 有某种缺省的颜色，通过在 `defclass` 里替这个槽指定一个 `:initform` ：

```
(defclass screen-circle (circle graphic)
  ((color :initform 'purple)))

```

现在 `screen-circle` 的实例缺省会是紫色的：

```
> (graphic-color (make-instance 'screen-circle))
PURPLE
```



## 11.5 优先级 (Precedence)

我们已经看过类别是怎样能有多个基类了。当一个实例的方法同时属于这个实例所属的几个类时，Lisp 需要某种方式来决定要使用哪个方法。优先级的重点在于确保这一切是以一种直观的方式发生的。

每一个类别，都有一个优先级列表：一个将自身及自身的基类从最具体到最不具体所排序的列表。在目前看过的例子中，优先级还不是需要讨论的议题，但在更大的程序里，它会是一个需要考虑的议题。

以下是一个更复杂的类别层级：

```
(defclass sculpture () (height width depth))

(defclass statue (sclpture) (subject))

(defclass metalwork () (metal-type))

(defclass casting (metalwork) ())

(defclass cast-statue (statue casting) ())
```



？？？

优先级的主要目的是，当一个通用函数 (generic function)被调用时，决定要用哪个方法。这个过程在下一节讲述。另一个优先级重要的地方是，当一个槽从多个基类继承时。408 页的备注解释了当这情况发生时的应用规则。



## 11.6 通用函数 (Generic Functions)

**类似于Java中的重载方法**



## 11.7 辅助方法 (Auxiliary Methods)

**AOP切面编程**

方法可以通过如 `:before` ， `:after` 以及 `:around` 等辅助方法来增强。 `:before` 方法允许我们说：“嘿首先，先做这个。” 最具体的 `:before` 方法**优先**被调用，作为其它方法调用的序幕 (prelude)。 `:after` 方法允许我们说 “P.S. 也做这个。” 最具体的 `:after` 方法**最后**被调用，作为其它方法调用的闭幕 (epilogue)。在这之间，我们运行的是在这之前仅视为方法的方法，而准确地说应该叫做主方法 (*primary method*)。这个主方法调用所返回的值为方法的返回值，甚至 `:after` 方法在之后被调用也不例外。

`:before` 与 `:after` 方法允许我们将新的行为包在调用主方法的周围。 `:around` 方法提供了一个更戏剧的方式来办到这件事。如果 `:around` 方法存在的话，会调用的是 `:around` 方法而不是主方法。则根据它自己的判断， `:around` 方法自己可能会调用主方法（通过函数 `call-next-method` ，这也是这个函数存在的目的）。



这称为标准方法组合机制 (*standard method combination*)。在标准方法组合机制里，调用一个通用函数会调用

1. 最具体的 `:around` 方法，如果有的话。

2. 否则，依序，

   > 1. 所有的 `:before` 方法，从最具体到最不具体。
   > 2. 最具体的主方法
   > 3. 所有的 `:after` 方法，从最不具体到最具体

返回值为 `:around` 方法的返回值（情况 1）或是最具体的主方法的返回值（情况 2）。

？？？



## 11.8 方法组合机制 (Method Combination)

？？？？？？？？？



## 11.9 封装 (Encapsulation)

面向对象的语言通常会提供某些手段，来区别对象的表示法以及它们给外在世界存取的介面。隐藏实现细节带来两个优点：你可以改变实现方式，而不影响对象对外的样子，而你可以保护对象在可能的危险方面被改动。隐藏细节有时候被称为封装 (*encapsulated*)。

虽然封装通常与面向对象编程相关联，但这两个概念其实是没相干的。你可以只拥有其一，而不需要另一个。我们已经在 108 页 (**译注：** 6.5 小节。)看过一个小规模的封装例子。函数 `stamp` 及 `reset` 通过共享一个计数器工作，但调用时我们不需要知道这个计数器，也保护我们不可直接修改它。

在 Common Lisp 里，包是标准的手段来区分公开及私有的信息。要限制某个东西的存取，我们将它放在另一个包里，并且针对外部介面，仅输出需要用的名字。

我们可以通过输出可被改动的名字，来封装一个槽，但不是槽的名字。举例来说，我们可以定义一个 `counter` 类别，以及相关的 `increment` 及 `clear` 方法如下：

```
(defpackage "CTR"
  (:use "COMMON-LISP")
  (:export "COUNTER" "INCREMENT" "CLEAR"))

(in-package ctr)

(defclass counter () ((state :initform 0)))

(defmethod increment ((c counter))
  (incf (slot-value c 'state)))

(defmethod clear ((c counter))
  (setf (slot-value c 'state) 0))

```

在这个定义下，在包外部的代码只能够创造 `counter` 的实例，并调用 `increment` 及 `clear` 方法，但不能够存取 `state` 。

如果你想要更进一步区别类的内部及外部介面，并使其不可能存取一个槽所存的值，你也可以这么做。只要在你将所有需要引用它的代码定义完，将槽的名字 unintern：

```
(unintern 'state)

```

则没有任何合法的、其它的办法，从任何包来引用到这个槽。



## 11.10 两种模型 (Two Models)

面向对象编程是一个令人疑惑的话题，部分的原因是因为有两种实现方式：消息传递模型 (message-passing model)与通用函数模型 (generic function model)。一开始先有的消息传递。通用函数是广义的消息传递。

在消息传递模型里，方法属于对象，且方法的继承与槽的继承概念一样。要找到一个物体的面积，我们传给它一个 `area` 消息：

```
tell obj are
```

而这调用了任何对象 `obj` 所拥有或继承来的 area 方法。

有时候我们需要传入额外的参数。举例来说，一个 `move` 方法接受一个说明要移动多远的参数。如我我们想要告诉 `obj` 移动 10 个单位，我们可以传下面的消息：

```
(move obj 10)
```

消息传递模型的局限性变得清晰。在消息传递模型里，我们仅特化 (specialize) 第一个参数。 牵扯到多对象时，没有规则告诉方法该如何处理 ── 而对象回应消息的这个模型使得这更加难处理了。

在消息传递模型里，方法是对象所有的，而在通用函数模型里，方法是特别为对象打造的 (specialized)。 如果我们仅特化第一个参数，那么通用函数模型和消息传递模型就是一样的。但在通用函数模型里，我们可以更进一步，要特化几个参数就几个。这也表示了，功能上来说，消息传递模型是通用函数模型的子集。如果你有通用函数模型，你可以仅特化第一个参数来模拟出消息传递模型。

？？？？？？？？？？？？

 























