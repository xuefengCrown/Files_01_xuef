## Functions

```python
>>> b = lambda x: lambda: x  # Lambdas can return other lambdas!
>>> c = b(88)
>>> c
<function <lambda> at ...

>>> d = lambda f: f(4)  # They can have functions as arguments as well.
>>> def square(x):
...     return x * x
>>> d(square)
16
```

```python
>>> z = 3
>>> e = lambda x: lambda y: lambda: x + y + z
>>> e(0)(1)()
4
```

### Lambdas and Currying

```python
def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    """
    "*** YOUR CODE HERE ***"
    return lambda x: lambda y: f(x,y)
```

```python
>>> import operator as op
>>> lambda_curry2 = lambda f: lambda x: lambda y: f(x,y)
>>> curried_add = lambda_curry2(op.add)
>>> curried_add
<function <lambda> at 0x038CDD30>
>>> add_three = curried_add(3)
>>> add_three(5)
8
```

### Composite Identity Function

```python
def compose1(f, g):
    """Return the composition function which given x, computes f(g(x))."""
    return lambda x: f(g(x))
```

### Recursion

#### Mutual Recursion

is Even and is Odd

#### Tree Recursion

##### Count Partitions

how to break problems

```python
1. use a 4
2. don't use a 4
we can capture all the possibilities
```



## Sequences

### List Comprehension

```python
[exp for _ in <seq> if ...]
# exp可以是列表
>>> [[e,e] for e in lst]
[[1, 1], [2, 2], [3, 3]]
```

### Identity vs Equality

the equality ope(==) checks whether 2 exps evaluate to equal values.

the identity comparison ope(is) checks whether 2 exps evaluate 2 the same object.

## Tree

1. A Tree has a root label and a list of branches.
2. Each branch is a tree

```python
def tree(root_label, branches=[]): # constructor
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root_label] + list(branches)
def label(tree): # selector
    return tree[0]
def branches(tree): # selector
    return tree[1:]
def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True
def is_leaf(tree):
    return not branches(tree)

```















