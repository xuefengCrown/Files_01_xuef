
"""
问题
怎样找出一个序列中出现次数最多的元素呢？

毫无疑问， Counter 对象在几乎所有需要制表或者计数数据的场合是非常有用的工具。
在解决这类问题的时候你应该优先选择它，而不是手动的利用字典去实现。
"""
# 先假设你有一个单词列表并且想找出哪个单词出现频率最高。
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counts = Counter(words)
print(word_counts)
# 出现频率最高的3个单词
top_three = word_counts.most_common(3)
print(top_three)
# Outputs [('eyes', 8), ('the', 5), ('look', 4)]
