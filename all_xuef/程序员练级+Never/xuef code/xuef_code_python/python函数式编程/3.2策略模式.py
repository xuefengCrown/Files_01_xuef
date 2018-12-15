
#Here is an example of a callable object with an embedded Strategy object:
import collections


class Mersenne1(collections.Callable):
    def __init__(self, algorithm):
        self.pow2= algorithm

    def __call__(self, arg):
        return self.pow2(arg)-1
