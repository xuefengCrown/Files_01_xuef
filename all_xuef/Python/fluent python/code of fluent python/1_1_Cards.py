"""
示例 1-1　一摞有序的纸牌
"""

import collections
import random

"""用 collections.namedtuple 构建了一个简单的类来表示一张纸牌"""
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    # class variable
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits
                       for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]

mydeck = FrenchDeck() # 生成一副牌
# 有多少张
print(len(mydeck))
# 从这副牌中抽取一张牌(第一张和最后一张)
print(mydeck[0],mydeck[-1])

# 从这副牌(序列)中随机抽取一张牌
print(random.choice(mydeck))

"""
因为 __getitem__ 方法把 [] 操作交给了 self._cards 列表，所以我
们的 deck 类自动支持切片（slicing）操作。
下面列出了查看一摞牌最上面 3 张和只看牌面是 A 的牌的操作。
"""
#print(mydeck[:3], end="\n\n")
# 其中第二种操作的具体方法是，先抽出索引是 12 的那张牌，然后每隔 13 张牌拿 1 张：
#print(mydeck[12::13])

# 另外，仅仅实现了 __getitem__ 方法，这一摞牌就变成可迭代的了：
##for card in mydeck:
##    print(card)
##
##for card in reversed(mydeck):
##    print(card)


"""
迭代通常是隐式的，譬如说一个集合类型没有实现 __contains__ 方法，
那么 in 运算符就会按顺序做一次迭代搜索。
"""
Card('Q', 'hearts') in mydeck


"""
那么排序呢？我们按照常规，用点数来判定扑克牌的大小，2 最小、A
最大；同时还要加上对花色的判定，黑桃最大、红桃次之、方块再次、
梅花最小。
"""
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank) # card rank 在ranks中的index
    return rank_value * len(suit_values) + suit_values[card.suit]
for card in sorted(mydeck, key=spades_high):
    print(card)


