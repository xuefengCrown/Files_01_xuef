### code is data
In Scheme, source code is data. Every non-primitive expression is a list, and we can write 
procedures that manipulate other programs just as we write procedures that manipulate lists.

Rewriting programs can be useful: we can write an interpreter that only handles a small core 
of the language, and then write a procedure that converts other special forms into the core 
language before a program is passed to the interpreter.

For example, the let special form is equivalent to a call expression that begins with a lambda expression. 
Both create a new frame extending the current environment and evaluate a body within that new environment.

```scheme
(let ((x 42) (y 16)) (+ x y))
;; Is equivalent to:
((lambda (x y) (+ x y)) 42 16)
```

We can use this rule to rewrite all let special forms into lambda expressions. 
We prevent evaluation of a program by quoting it, and then pass it to a procedure called let-to-lambda:

```scheme
scm> (let-to-lambda '(let ((a 1) (b 2)) (+ a b)))
((lambda (a b) (+ a b)) 1 2)
scm> (let-to-lambda '(let ((a 1)) (let ((b a)) b)))
((lambda (a) ((lambda (b) b) a)) 1)
```

In order to handle all programs, let-to-lambda must be aware of Scheme syntax. 
Since Scheme expressions are recursively nested, let-to-lambda must also be recursive. 
In fact, the structure of let-to-lambda is somewhat similar to that of scheme_eval--but in Scheme!

(define (let-to-lambda expr)
  (cond ((atom?   expr) <rewrite atoms>)
```scheme
    ((quoted? expr) <rewrite quoted expressions>)
    ((lambda? expr) <rewrite lambda expressions>)
    ((define? expr) <rewrite define expressions>)
    ((let?    expr) <rewrite let expressions>)
    (else           <rewrite other expressions>)))
```
Implement the let-to-lambda procedure, which takes in an expression and rewrites all of the 
let special forms in the expression into their equivalent lambda expressions.

Hint: You may want to implement map and zip at the top of questions.scm.

```scheme
scm> (zip '((1 2) (3 4) (5 6)))
((1 3 5) (2 4 6))
scm> (zip '((1 2)))
((1) (2))
scm> (zip '())
(() ())
```



尾调用由于是函数的最后一步操作，所以不需要保留外层函数的调用记录，因为调用位置、内部变量等信息都不会再用到了，只要直接用内层函数的调用记录，取代外层函数的调用记录就可以了。

> ```
> function f() {
>   let m = 1;
>   let n = 2;
>   return g(m + n);
> }
> f();
>
> // 等同于
> function f() {
>   return g(3);
> }
> f();
>
> // 等同于
> g(3);
>
> ```

上面代码中，如果函数g不是尾调用，函数f就需要保存内部变量m和n的值、g的调用位置等信息。但由于调用g之后，函数f就结束了，所以执行到最后一步，完全可以删除 f() 的调用记录，只保留 g(3) 的调用记录。

```python
def tailrecsum(x, total=0):
    if x == 0:
      return total
    else:
      return tailrecsum(x - 1, total + x) ;; 不必新开栈帧，直接在当前栈帧执行!
```



```scheme
(define (pyth x y)
 (sqrt (+ (* x x) (* y y))))
```

```scheme
(define (pyth& x y k)
 (*& x x (lambda (x2)
          (*& y y (lambda (y2)
                   (+& x2 y2 (lambda (x2py2)
                              (sqrt& x2py2 k))))))))
```

```scheme
(define (*& x y k)
 (k (* x y)))
```