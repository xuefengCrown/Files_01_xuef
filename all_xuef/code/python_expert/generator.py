#coding:utf-8

"""
a basic generator
"""

def step(start=0, step=1):
    _start = start
    while True:
        yield _start
        _start += step
        
stepper = step(10, 2)

print(stepper.__next__())
print(stepper.__next__())
print(stepper.__next__())

# what will list(stepper) do?
# don't do this! in this case, it will run out of memory

## let's fix it

def step_with_end(start=0, step=1, end=100):
    _start = start
    while _start < end:
        yield _start
        _start += step






















