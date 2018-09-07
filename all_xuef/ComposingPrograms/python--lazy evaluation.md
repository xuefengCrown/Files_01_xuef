## Lazy Evaluation

### definition

```
delays evaluation of an expression until its value is needed. Some benefits:
1. The ability to define control flow(if, and, or)
2. The ability to define potentially infinite data structures.
```

### Iterators

```
iter(iterable): Return an iterator
next(iterator): Return the next element

>> s = [1,2,3]
>> one, two = iter(s), iter(s)
>> next(one)
1
>> three = iter(two) # two, three 同步
```

### for ... in 的内在机制

```
counts = [1,2,3]
items = iter(counts)
try:
	while True:
		item = next(items)
		print(item)
except StopIteration:
	pass
```



### Built-in Functions for Iteration

Many built-in Python sequence operations return iterators that compute results lazily.

```python
map(func, iterable): Return an iterator that iterates over func(x) for x in iterable
filter(func, iterable)
zip(iterable1, iterable2): Returns an iterator that iterates co-indexed (x, y) pairs
reversed(sequence): Return an iterator that iterates over a sequence in reverse order. Note this only works on ordered collections.
```

To view the contents of an iterator, place the resulting elements into a container.

```python
list(iterable)
tuple(iterable)
sorted(iterable)
```

### Generators

Generator: An iterator created automatically by calling a generator function.

#### yield from

```python
def a_then_b(a, b):
    for x in a:
        yield x
    for x in b:
        yield x
def a_then_b(a, b):
    yield from a
    yield from b
```

```python
def countdown(K):
    if K > 0:
        yield K
        yield from countdown(K-1)
```

### Streams

#### definition

Streams: Are lazily computed pairs.

They are analogous to lazily computed Scheme lists.



## Tail Recursion

In Scheme, a frame can be removed if there is no further work to be done.

no additional work to be done after making the recursive call.



## Interpreter

### Reading input

Lexical analysis: Turning the inout string into a collection of tokens.

```
A token is a single unit of the input string, e.g. literals,names, keywords, delimiters
```

Syntatic analysis: Turning tokens into representation of the expression in the implementing language.

```
we want to turn the scheme expression and be able to represent that expression in python.
```

### Representing Scheme primitive expr

1. self-evaluating expr (booleans and nums)

```
use python booleans and python nums
```

2. Symbols

use Python strings

3. Combinations

Python pairs

```python
class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def __repr__(self):
        return 'Pair({0},{1})'.format(self.first, self.second)

 class nil:
    def __repr__(self):
        return 'nil'
 nil = nil()
```

### one special case: quote

Recall that the quote special form can be invoked in two ways:

```scheme
(quote <expr>)
'<expr>
```

### Eval

After reading exprs, we can then eval them to obtain values.

Rules for obtain an expression depends on the expression's type.

```
Types of Scheme expressions: self-evaluating expressions, symbols, call expressions, special form expr.
```

#### Frames and Environments

```
Symbols are looked up in the current environment, which consists of the current frame, its parent frame, and all its ancestor frames until the Global Frame.
```

```scheme
(define (make-adder x)
  	(lambda (y) (+ x y)))
(define add-three (make-adder 3))
(add-three 5)
(add-three 10)
```

#### Frames in our interpreter

Frames are represented in our interpreter as instance of the Frame class

Each Frame instance has two instance attributes:

```
bindings: a dictionary that binds Scheme symbols(Python strings) to Scheme values
parent: the parent frame, another Frame instance
```

The evaluator needs to know the current environment, given as a single Frame instance, in order to look up names in expressions.

#### Evaluating primitive expr

self-evaluating expr: These expr evaluate to themselves.

Symbols:

1. Look in the current frame for the symbol. If it's found, return the value bound to it.
2. If it's not found in the current frame, look in the parent frame. If it's not found in the current frame, look in its parents frame, and so on.
3. If the global frame is reached and the name is not found, raise a SchemeError.

#### Evaluating combinations

```scheme
(<operator> <operand1> <operand2> ...)
# The operator of a combination tells us whether it's a special form expression or a call expression.
```

If the operator is a symbol and is found in the dictionary of special forms, the combination is a special form.

```
eacj special form has special rules for evaluation(see Scheme lecture)
```

Otherwise, the combination is a call expression.

```
step1. Evaluate the operator to get a procedure.
step2. Evaluate the operands from left to right.
step3. Apply the procedure to the values of the operands.
```

!!! first two steps are recursive calls to eval.

#### Apply procedure

A biult-in procedure is a procedure that is predefined in our Scheme interpreter, e.g. +, list, modulo, etc.

```
1. each biult-in procedure has a corresponding Python function that performs the appropriate operation.
2. In our interpreter--instances of the BuiltinProcedure class
```

A user-defined procedure is a procedure defined by the user, either with a lambda expression or a define expression.

```
Each user-defined procedure has:
1) a list of formal parameters.
2) a body(which is a Scheme list)
3) and a parent frame
In our interpreter, instances of the LambdaProcedure class
(包括define定义的具名函数和匿名函数)
```

#### User-defined procedures

```scheme
(define (square x) (* x x))
```

Applying user-defined procedures:

1. open a new frame whose parent is the parent frame of the procedure being applied.

   函数被定义时所在的 env, 即为它的 parent frame

2. Bind the formal parameters of the procedure to the arguments in the new frame.

3. Evaluate the body of the procedure in the frame.

#### The evaluator

The evaluator consists of two mutually-recursive(互相调用的递归) components:

```
Eval:
Base cases:
1. self-evaluating expressions
2. look up values bound to symbols
Recursive cases:
1. Eval(operator), Eval(o) for each operand o
2. Apply(proc, args)
3. Eval(expr) for expression expr in the body of special forms
```

```
Apply:
Base cases:
1. Built-in procedures
Recursive cases:
1. Eval(body) of user edfined procedures
```

!!! They call each other

#### A new special form

The let special form allows us to create a temporary frame inorder to execute its body.

```scheme
(let ((name1 expr1) (name2 expr2))
  <body>)
```

How to evaluate:

step1. Evaluate each of the expression in the bindings in the current frame.

step2. Create a new frame whose parent is the current frame.

step3. Inside the new frame, assign <name1> to the value of <expr1>, <name2> to the value of <expr2>, and so on.

step4. Evaluate <body>, which may be more than one expression, in the new frame.

step5. Close the new frame and resume(恢复) execution in the previous frame.









