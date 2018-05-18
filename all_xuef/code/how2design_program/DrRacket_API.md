# string

```lisp
(string-append "hello" " " "world")

> (+ (string-length "hello world") 20)
31
> (number->string 42)
"42"
> (string->number "42")
42
```

# operate-string

```lisp
(substring "hello" 1 4)->"ell"

```



# and 、or、 not

```lisp
> (and #true #true)
#true

> (and #true #false)
#false

> (or #true #false)
#true

> (or #false #false)
#false

> (not #false)
#true
```

# function

```lisp
(define (y x) (* x x))

```

# math func

```lisp
(sin 0)
```



# conditional

## cond

```lisp
(define (sign x)
  (cond
    [(> x 0) 1]
    [(= x 0) 0]
    [(< x 0) -1]))
```

## if

```lisp
(if 
 (= x 0) 
 0 
 (/ 1 x))
```



# predicate

```lisp
> (number? 4)
#true

> (number? pi)
#true

string?
rational?
```



# constant（常量）

```lisp
(define HEIGHT 60)
```



# compare

## string

```lisp
# 比较词语顺序，而不是长度
string<?
string=?
string>?
```



