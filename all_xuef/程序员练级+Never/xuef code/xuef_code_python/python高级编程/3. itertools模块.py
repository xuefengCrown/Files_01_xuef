
# C编写的，覆盖很多迭代模式

import itertools as its

# islice 迭代器上的滑动窗口
# tee 往返式
# groupby


# chain
# cycle
import time
for i in its.cycle(['aa','bb','cc']):
    print(i)
    time.sleep(1)

# izip
