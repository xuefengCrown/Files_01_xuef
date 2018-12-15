
map(function, zip(one_iterable, another_iterable))

#We can also look at it like this:
(function(x,y) for x,y in zip(one_iterable, another_iterable))

#We might have the idea of generalizing the whole thing to this:
def star_map(function, *iterables)
    return (function(*args) for args in zip(*iterables))
