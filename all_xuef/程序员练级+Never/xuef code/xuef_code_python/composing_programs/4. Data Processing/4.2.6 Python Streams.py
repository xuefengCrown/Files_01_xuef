"""
Streams offer another way to represent sequential data implicitly.
A stream is a lazily computed linked list.

Like an Link, the rest of a Stream is itself a Stream.
Unlike an Link, the rest of a stream is only computed when it is looked up,
rather than being stored in advance. That is, the rest of a stream is computed lazily.

"""
##To achieve this lazy evaluation, a stream stores a function that computes the rest of the stream.
##Whenever this function is called, its returned value is cached as part of the stream in an
##attribute called _rest, named with an underscore to indicate that it should not be accessed
##directly.

class Stream:
    """A lazily computed linked list."""
    class empty:
        def __repr__(self):
            return 'Stream.empty'
    empty = empty()
    def __init__(self, first, compute_rest=lambda: empty):
        assert callable(compute_rest), 'compute_rest must be callable.'
        self.first = first
        self._compute_rest = compute_rest
    @property
    def rest(self):
        """Return the rest of the stream, computing it if necessary."""
        if self._compute_rest is not None:
            self._rest = self._compute_rest()
            self._compute_rest = None
        return self._rest
    def __repr__(self):
        return 'Stream({0}, <...>)'.format(repr(self.first))

#r = Link(1, Link(2+3, Link(9)))

##Here, 1 is the first element of the stream, and the lambda expression that
##follows returns a function for computing the rest of the stream.
s = Stream(1, lambda: Stream(2+3, lambda: print(9)))

# the rest of s includes a function to compute the rest;


##increasing integers
##Lazy evaluation gives us the ability to represent infinite sequential datasets using streams.
##For example, we can represent increasing integers, starting at any first value.

##def integer_stream(first):
##    def compute_rest():
##        return integer_stream(first+1)
##    return Stream(first, compute_rest)
    
def integer_stream(first):
    # integer_stream is actually recursive because this stream's compute_rest
    # calls integer_stream again
    return Stream(first, lambda: integer_stream(first+1))

positives = integer_stream(1)
print(positives)

rg = integer_stream(5)
while 1:
    print(rg.first)
    rg = rg.rest


def map_stream(fn, s):
    if s is Stream.empty:
        return s
    def compute_rest():
        return map_stream(fn, s.rest)
    return Stream(fn(s.first), compute_rest)
