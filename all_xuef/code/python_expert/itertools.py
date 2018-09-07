from itertools import chain
from itertools import combinations
from itertools import permutations
from itertools import compress

my_lst = 'abcdef'
my_selector = [1,0,1,1,0,1]

print(list(compress(my_lst, my_selector)))
