### mapcar

```lisp
> (mapcar #'- '(1 2 3))
(-1 -2 -3)
> (mapcar #'+ '(1 2 3) '(10 20 30))
(11 22 33)
```

### maplist

```lisp
> (setf mon '(31 28 31 30 31 30 31 31 30 31 30 31))
(31 28 31 30 31 30 31 31 30 31 30 31)
> (setf nom (reverse mon))
(31 30 31 30 31 31 30 31 30 31 28 31)
> (setf sums (maplist #'(lambda (x)
                          (apply #'+ x))
                      nom))
(365 334 304 273 243 212 181 151 120 90 59 31)
```

### mapcan

???

