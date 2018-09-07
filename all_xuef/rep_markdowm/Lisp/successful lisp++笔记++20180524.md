

# chap1

## Lisp擅长什么

Lisp is also used as an extension language because of its simple, consistent syntax and the ability for system designers to add new functions to Lisp without writing an entire new language. The Emacs editor
and the AutoCAD drafting（制图） program are two of the best examples of this use of Lisp.

And of course Lisp is still the language most often used for research in artificial intelligence and
advanced computer language design, but we won't touch on either of those subjects in this book. When
you've finished this book, you'll have the knowledge needed to recognize what problems you should
solve using Lisp, and how to approach the solution's design.



# chap3 Basic

## list

```lisp
So the following are also lists:
()
(())
((()))
((a b c))
((1 2) 3 4)
(mouse (monitor 512 342) (keyboard US))
(defun factorial (x) (if (eql x 0) 1 (* x (factorial (- x 1)))))
```

A list can be a lot of things in Lisp. In the most general sense, a list can be either a program or
data. And because lists can themselves be made of other lists, you can have arbitrary
combinations of data and programs mixed at different levels of list structure -- this is what makes
Lisp so flexible for those who understand it, and so confusing for those who don't.

## atom

```lisp
Accordingly, these words and numbers are all atoms:
1
25
342
mouse
factorial
x
```

Since an atom can be marked off by either whitespace or a parenthesis, we could eliminate any
whitespace between an atom and a parenthesis, or between two parentheses. Thus, the following
two lists are identical:

```lisp
(defun factorial (x) (if (eql x 0) 1 (* x (factorial (- x 1)))))
(defun factorial(x)(if(eql x 0)1(* x(factorial(- x 1)))))
```

## A form 

is meant to be evaluated

A form can be either an atom or a list. The important thing is that the form is meant to be evaluated.



Evaluation is simple if the form is an atom. Lisp treats the atom as a name, and retrieves the value for
the name (if a value exists).



## 你是谁（谓词）

还得看是在什么维度和意义下问这个问题

```lisp
(atom 123)
T
(numberp 123)
T
(atom :foo)
T
(numberp :foo)
NIL
```

## true && false

NIL is the only false value in Lisp -- everything else is true.

Unless a predicate has a more useful value to return, it conventionally returns T to mean true. 



## evaluate process

Lisp always does the same thing to evaluate a list form:（递归的）

1. Evaluate the arguments, from left to right.
2. Get the function associated with the first element.
3. Apply the function to the arguments.

另外，递归得有终止条件

```lisp
Numbers and keywords are self-evaluating. So are strings. The *FEATURES* variable is predefined by Lisp -- your system will probably return a different value.
```

## Special forms and macros

Special forms and macros change argument evaluation

So if a list form isn't always a function call, what else can it be? There are two cases, but the result is the
same: some arguments are evaluated, and some aren't.

There are two kinds of forms that don't evaluate all of their arguments: special forms and macros. Lisp
predefines a small number of special forms. You can't add your own special forms -- they're primitive
features of the language itself. 



## function

A function can return any number of values

### Arguments are usually not modified by a function

I mentioned earlier that you can pass a location to a function, and have the function change the location's
value. This is a very uncommon practice for a Lisp program, even though other languages make it part
of their standard repertoire.

You could specify the location to be modified as either a non-keyword symbol or a composite value --
obviously, you can't modify a constant. If you provide a symbol, then your function must execute code
to give the symbol a new value. If you provide a composite data structure, your function must execute
code to change the correct piece of the composite value. It's harder to write Lisp code to do this, and it's
harder to understand programs written this way. So Lisp programmers usually write functions that get
their inputs from parameters, and produce their outputs as the function result.



## setq

```lisp
(setq month "June" day 8 year 1954)
1954
```



## let

```lisp
(let ((p 52.8)
      (q 35.9)
      (r (f 12.07)))
    (g 18.3)
    (f p)
    (f q)
    (g r t))
```

```lisp
(setq a 89)
89

(let ((a 3))
    (+ a 2))
5

a
89
```



```lisp
Unlike SETQ, which assigns values in left-to-right order, LET binds variables all at the same time:
(setq w 77)
77
(let ((w 8)
	  (x w))
	(+ w x))
85
LET bound W to 8 and X to W. Because these bindings happened at the same time, W still had its value of 77.

Lisp has a variation of LET, called LET*, that does perform bindings in order:
(setq u 37)
37
(let* ((v 4)
	   (u v))
	(+ u v))
8
```



## COND

The COND macro lets you evaluate Lisp forms conditionally. Like LET, COND uses parentheses to
delimit different parts of the form.



The clauses are selected in order -- as soon as one test succeeds, the corresponding
body forms are evaluated and the value of the last body form becomes the value of the COND form.

```lisp
(let ((a 32))
  (cond ((eql a 13) "An unlucky number")
        ((eql a 99) "A lucky number")
        (t "Nothing special about this number")))
"Nothing special about this number"
```



## QUOTE

\``````````````````````



## cons

Putting things together, and taking them apart

```lisp
()
'()
nil
```



## LIST FIRST and REST



## A symbol is just a name

A symbol is just a name. It can stand for itself. This makes it easy to write certain kinds of programs in
Lisp. For example, if you want your program to represent relationships in your family tree, you can
make a database that keeps relationships like this:
(father John Barry)
(son John Harold)
(father John Susan)
(mother Edith Barry)
(mother Edith Susan)
...
Each relationship is a list. (father John Barry) means that John is Barry's father. Every element
of every list in our database is a symbol. Your Lisp program can compare symbols in this database to
determine, for example, that Harold is Barry's grandfather. If you tried to write a program like this in
another language -- a language without symbols -- you'd have to decide how to represent the names of
family members and relationships, and then create code to perform all the needed operations -- reading,
printing, comparison, assignment, etc. This is all built into Lisp, because symbols are a data type distinct
from the objects they might be used to name.



## macro

Macros return a form, not values

When Lisp evaluates a call to your macro, it first evaluates the body of your macro definition, then evaluates the result of the first evaluation.

```lisp
(defmacro setq-literal (place literal)
	`(setq ,place ',literal))
SETQ-LITERAL
(setq-literal a b)
B
a
B

(defmacro reverse-cons (rest first)
	`(cons ,first ,rest))
REVERSE-CONS
(reverse-cons nil A)
(B)

(macroexpand '(setq-literal a b))
(SETQ A 'B)
(macroexpand '(reverse-cons nil a))
(CONS A NIL)
```



## VALUES

```lisp
(values)
(values :this)
:THIS
(values :this :that)
:THIS
:THAT
```

A few special forms receive multiple values
What might you want to do with multiple values in a program? The most basic operations are to:

1. bind each value to a separate symbol, or

2. collect the values into a list.
  Use MULTIPLE-VALUE-BIND to bind each value to a separate symbol:

  ```lisp
  (multiple-value-bind (a b c) (values 2 3 5)
  	(+ a b c))
  10

  (multiple-value-bind (a b c) (values 2 3 5 'x 'y)
  	(+ a b c))
  10
  ```

  ​

## Other Data Types

Lisp almost always does the right thing with numbers



So how does Lisp manage to do the right thing with numbers? After all, it seems like these problems are
inherent in computer arithmetic. The answer is that Lisp doesn't do use just the built-in computer
arithmetic operations -- it adds certain mathematically accurate numeric data types:

+ bignums are integers with an unlimited number of digits (subject only to limitations of computer

memory)

+ rational numbers are the exact quotient of two integers, not a floating point number resulting

from an approximate machine division algorithm

```lisp
(/ 1 3)
1/3
(+ (/ 7 11) (/ 13 31))
360/341
```

```lisp
(float (/ 1 3))
0.3333333333333333
(* (float (/ 1 10)) (float (/ 1 10)))
0.010000000000000002
```



## read and write

Characters give Lisp something to read and write



## Arrays organize data into tables

```lisp
(setq a1 (make-array '(3 4)))
#2A	((NIL NIL NIL NIL)
	(NIL NIL NIL NIL)
	(NIL NIL NIL NIL))
(setf (aref a1 0 0) (list 'element 0 0))
(ELEMENT 0 0)
(setf (aref a1 1 0) (list 'element 1 0))
(ELEMENT 1 0)
(setf (aref a1 2 0) (list 'element 2 0))
(ELEMENT 2 0)
a1
#2A	(((ELEMENT 0 0) NIL NIL NIL)
	((ELEMENT 1 0) NIL NIL NIL)
	((ELEMENT 2 0) NIL NIL NIL))
```

SETQ assigns a value to a symbol, SETF assigns a value to a place. 



## Vectors are one-dimensional arrays

```lisp
(setq v1 (make-array '(3)))
#(NIL NIL NIL)
(make-array 3)
#(NIL NIL NIL)
(setf (aref v1 0) :zero)
:ZERO
(setf (aref v1 1) :one)
:ONE
(aref v1 0)
:ZERO
v1
#(:ZERO :ONE NIL)
```

```lisp
(vector 34 22 30)
#(34 22 30)

You can use AREF to access the elements of a vector, or you can use the sequence-specific function, ELT:
(setf v2 (vector 34 22 30 99 66 77))
#(34 22 30 99 66 77)
(setf (elt v2 3) :radio)
:RADIO
v2
#(34 22 30 :RADIO 66 77)
```



## Strings are vectors that contain only characters

Vector 与 Array 都属于 Sequence

String 属于 Vector

You already know how to write a string using the "..." syntax. Since a string is a vector, you can
apply the array and vector functions to access elements of a string. 

```lisp
(setq s1 "hello, there.")
"hello, there."
(setf (elt s1 0) #\H))
#\H
(setf (elt s1 12) #\!)
#\!
s1
"Hello, there!"
(string 'a-symbol)
"A-SYMBOL"
(string #\G)
"G"
```



## Symbols

Symbols are unique, but they have many values

```lisp
For example, if your program represented and manipulated objects, you could store information about an object on its property list:
(setf (get 'object-1 'color) 'red)
RED
(setf (get 'object-1 'size) 'large)
LARGE
(setf (get 'object-1 'shape) 'round)
ROUND
(setf (get 'object-1 'position) '(on table))
(ON TABLE)
(setf (get 'object-1 'weight) 15)
15
(symbol-plist 'object-1)
(WEIGHT 15 POSITION (ON TABLE) SHAPE ROUND SIZE LARGE COLOR RED)
(get 'object-1 'color)
RED
object-1
Error: no value
```

Note that OBJECT-1 doesn't have a value -- all of the useful information is in two places: the identity of
the symbol, and the symbol's properties.



Properties are less often used in modern Lisp programs. Hash tables (see below), structures (described in
the next section), and CLOS objects (see Chapter 7 and Chapter 14) provide all of the capabilities of
property lists in ways that are easier to use and more efficient. Modern Lisp development systems often
use properties to annotate(注释) a program by keeping track of certain information such as the file and file
position of the defining form for a symbol, and the definition of a function's argument list (for use by
informational tools in the programming environment).



## Structures let you store related data

A Lisp structure gives you a way to create an object which stores related data in named slots.

```lisp
(defstruct struct-1 color size shape position weight)
STRUCT-1

(setq object-2 (make-struct-1
					:size 'small
                    :color 'green
                    :weight 10
                    :shape 'square))
#S(STRUCT-1 :COLOR GREEN :SIZE SMALL :SHAPE SQUARE :POSITION NIL :WEIGHT 10)

(struct-1-shape object-2)
SQUARE
(struct-1-position object-2)
NIL
(setf (struct-1-position object-2) '(under table))
(UNDER TABLE)
(struct-1-position object-2)
(UNDER-TABLE)
```

In the example, we defined a structure type named STRUCT-1 with slots named COLOR, SHAPE,
SIZE, POSITION, and WEIGHT. Then we created an instance of a STRUCT-1 type, and assigned the
instance to the variable OBJECT-2. The rest of the example shows how to access slots of a struct
instance using accessor functions named for the structure type and the slot name. Lisp generates the
make-structname and structname-slotname functions when you define a structure using DEFSTRUCT.



## Type information is apparent at runtime

```lisp
(type-of 123)
FIXNUM
(type-of 123456789000)
BIGNUM
(type-of "hello, world")
(SIMPLE-BASE-STRING 12)
(type-of 'fubar)
SYMBOL
(type-of '(a b c))
CONS
```



## Hash Tables provide quick data access from a lookup key

Hash Table 的本质是接近O(1)的检索能力。

A hash table associates a value with a unique key. Unlike a property list, a hash table is well suited to a
large number of key/value pairs, but suffers from excessive overhead for smaller sets of associations.

```lisp
(setq ht1 (make-hash-table))
#<HASH-TABLE>
(gethash 'quux ht1)
NIL
NIL
(setf (gethash 'baz ht1) 'baz-value)
BAZ-VALUE
(gethash 'baz ht1)
BAZ-VALUE
T

(setf (gethash 'gronk ht1) nil)
NIL
(gethash 'gronk ht1)
NIL
T
```

Java, Python 有着相同的字典检索语法

dictionary.get(key) // python中直接可以 dictionary[key]

Lisp 的 hash table 检索，语法有点反常 (gethash key dict)



You create a hash table using MAKE-HASH-TABLE, and access values using GETHASH. GETHASH
returns two values. The first is the value associated with the key. The second is T if the key was found,
and NIL otherwise. Notice the difference between the first and last GETHASH form in the examples
above.



By default, a hash table is created so that its keys are compared using EQ -- this works for symbols, but
not numbers or lists. We'll learn more about equality predicates in Chapter 17. For now, just remember
that if you want to use numbers for keys, you must create a hash table using the form:

```lisp
(make-hash-table :test #'eql)
```

If you want to use lists for keys, create your hash table with:

```lisp
(make-hash-table :test #'equal)
```

发挥你的想象力，你可以把任何东西做为key，可以将任何东西作为value

If you want to remove a key, use the form (REMHASH key hash-table). And if you want to
change the value for a key, use GETHASH with SETF, just as if you were adding a new key/value pair.



## Packages keep names from colliding(冲突)

```lisp
file "lib1"
file "lib2"
(load "lib1")
(rename-package UTIL UTIL-1)
(load "lib2")
(rename-package UTIL UTIL-2)
(UTIL-1:initailize)
```



## Essential Input and Output

READ turns characters into Lisp data.



## OPEN and CLOSE let you work with files

Normally, READ reads from the keyboard and PRINT prints to the screen.

You can attach a stream to a file using the OPEN function, which takes as parameters a file name and a
keyword argument to specify the direction (input or output) of the stream.

```lisp
(setq out-stream (open "my-temp-file" :direction :output))
#<OUTPUT-STREAM "my-temp-file">
(print 'abc out-stream)
ABC
(close out-stream)
T
(setq in-stream (open "my-temp-file" :direction :input))
#<INPUT-STREAM "my-temp-file">
(read in-stream)
ABC
(close in-stream)
```



## Variations on a PRINT theme

Lisp also provides a WRITE function to give you control over more details of printing, using keyword
arguments to control these options:



# chap4 loop

## function

### &optional

```lisp
(defun silly-list-1 (p1 p2 &optional p3 p4)
(list p1 p2 p3 p4))
SILLY-LIST-1
(silly-list-1 'foo 'bar)
(FOO BAR NIL NIL)
(silly-list-1 'foo 'bar 'baz)
(FOO BAR BAZ NIL)
(silly-list-1 'foo 'bar 'baz 'rux)
(FOO BAR BAZ RUX)
```

### &rest

If you want to have an indefinite number of parameters, you can name one parameter to receive a list of all the "extras" using the &REST symbol in the lambda list, like this:

```lisp
(defun silly-list-2 (p1 p2 &rest p3)
(list p1 p2 p3))
(silly-list-2 'foo 'bar)
(FOO BAR NIL)
(silly-list-2 'foo 'bar 'baz)
(FOO BAR (BAZ))
(silly-list-2 'foo 'bar 'baz 'bob 'tom 'don)
(FOO BAR (BAZ BOB TOM DON))
```

### Using global variables and constants

There are two more ways to define global variables in Lisp:

```lisp
(defvar *var1* 2)
*VAR1*

(defparameter *a-var* 3)
*A-VAR*
```



### Defining recursive functions

```lisp
> (null ())
T
```

```lisp
(defun my-length (list)
	(cond ((null list) 0)
		   (t (1+ (my-length (rest list))))))
```



跟踪调用

```lisp
(trace my-length)
NIL
(my-length '(a b c d))
```



### Tail recursion

```lisp
; Normal recursive call
(defun factorial (n)
  (cond ((zerop n) 1)
  		 (t (* ; * is the last function called
              n
              (factorial (- n 1))))))
; Tail-recursive call
(defun factorial-tr (n)
	(factorial-tr-helper n 1))
(defun factorial-tr-helper (n product)
	(cond ((zerop n) product)
          	(t
              ; factorial-tr-helper is the last function called
              (factorial-tr-helper (- n 1) (* product n)))))
```



### Reading, writing, and arithmetic

```lisp
(defun simple-adding-machine-1 ()
  (let ((sum 0)
  		next)
    (loop
    	(setq next (read))
    	(cond ((numberp next)
    			(incf sum next))
   			 ((eq '= next)
    			(print sum)
    			(return))
    		  (t
    			(format t "~&~A ignored!~%" next))))
    	(values)))
```



```lisp
A better way to write this kind of code uses WITH-OPEN-FILE:
(with-open-file (in-stream "infile.dat" :direction :input)
	(with-open-file (out-stream "outfile.dat" :direction :output)
		(let ((*standard-input* in-stream)
			  (*standard-output* out-stream))
			(declare (special *standard-input* *standard-output*))
			(simple-adding-machine-1))))
```



# chap5 Iteration

## loop

```lisp
(let ((n 0))
(loop
  (when (> n 10) (return))
  (print n) (prin1 (* n n))
  (incf n)))
```

## ditimes

```lisp
(dotimes (n 11)
	(print n) (prin1 (* n n)))
```



## dolist

```lisp
(dolist (item '(1 2 4 5 9 17 25))
	(format t "~&~D is~:[n't~;~] a perfect square.~%" item (integerp (sqrt item))))
```



## do

```lisp
(do ((which 1 (1+ which))
     (list '(foo bar baz qux) (rest list)))
    ((null list) 'done)
   (format t "~&Item ~D is ~S.~%" which (first list)))
```

```lisp
(do ((var1 init1 step1)
	 (var2 init2 step2)
	  ...)
	(end-test result)
  statement1
	...)
```



# chap6





# chap7 clos

```lisp
(defclass 3d-point () (x y x))
#<STANDARD-CLASS 3D-POINT>
```

```lisp
(defstruct 3d-point-struct x y z)
```

but the class actually has less functionality than the structure. The class does not define default accessors
for slots. To access the slots, you would have to use SLOT-VALUE as in this example:

```lisp
(let ((a-point (make-instance '3d-point))) # only 执行一次
  (setf (slot-value a-point 'x) 0) ; set the X slot
  (slot-value a-point 'x)) ; get the X slot
0
```



## 指定 accessors

```lisp
(defclass 3d-point ()
  ((x :accessor point-x)
  (y :accessor point-y)
  (z :accessor point-z)))

(let ((a-point (make-instance '3d-point)))
	(setf (point-x a-point) 0)
	(point-x a-point))
0
```



```lisp
(defclass 3d-point ()
  ((x :reader get-x :writer set-x)
  (y :reader get-y :writer set-y)
  (z :reader get-z :writer set-z)))
#<STANDARD-CLASS 3D-POINT>
(let ((a-point (make-instance '3d-point)))
  (set-z 3 a-point)
  (get-z a-point))
```



```lisp
(defclass sphere ()
   ((x :accessor x)
    (y :accessor y)
    (z :accessor z)
    (radius :accessor radius)
    (volume :reader volume)
    (translate :writer translate)))
#<STANDARD-CLASS SPHERE>
```























































