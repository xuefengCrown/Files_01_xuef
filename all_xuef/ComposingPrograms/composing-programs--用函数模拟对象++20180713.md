

## 模拟银行账户

```python
def make_withdraw(balance):
    """Return a withdraw function that draws down balance with each call."""
    def withdraw(amount):
        nonlocal balance                 # Declare the name "balance" nonlocal
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount       # Re-bind the existing balance name
        return balance
    return withdraw
```

这里功能还很有限，只能取钱，不能存钱；可以定义一个 make_account， 返回一个操作入口，以支持存取钱操作。

### 不使用 nonlocal

Mutable values can be changed without a nonlocal statement.

```python
def make_withdraw(balance):
    """Return a withdraw function that draws down balance with each call."""
    b = [balance]
    def withdraw(amount):
        if amount > b[0]:
            return 'Insufficient funds'
        b[0] = b[0] - amount     
        return balance
    return withdraw
```

### mutable 操作的破坏性

Referential Transparency, Lost

Exps are Referential Transparency if substituting an expression with its value does not change the meaning of a program.

```python
mul(add(2, mul(4, 6), add(3, 5)))
mul(add(2, 24       , add(3, 5)))
mul(add(26          , add(3, 5)))
```

Mutation operations violate the condition of Referential Transparency because they do more than just return a value: They change the environment.

看一个例子

```python
def f(x):
    x = 4
    def g(y):
        def h(z):
            nolocal x
            x = x + 1
            return x + y + z
        return h
    return g
a = f(1)
b = a(2)
total = b(3) + b(4) # total = 10 + b(4)     
# b(3)单独执行的结果 + b(4)单独执行的结果 != 同时执行的结果 
```



