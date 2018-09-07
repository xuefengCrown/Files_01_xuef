你得了解解释器，站在解释器的角度，你才能理解语言！

## define 做了什么

```python
(define x <exp>)
1. 求值exp
2. Bind the resulting value to the given name in the current frame.
3. Return the name as a symbol.
```



## 赋值操作

```python
x = y # 将=右边表达式的值复制给左边变量
```

## lambda

```python
1. Create a lambda procedure with the given parameters and body.
2. Return the lambda procedure.
```

注意： The body expression is evaluated when the lambda procedure is applied.

## Class

### Class Statement

A class statement creates a new class and binds that class to the current environment.

Assignment & def statements in the <suite> create class attributes.

```python
class <name>:
    <suite>
```

### when class is called

```
1. A new instance of that class is created.
2. The __init__ method of a class is called with the new object as its first argument(named self), along with additional arguments provided in the call expression.
```









