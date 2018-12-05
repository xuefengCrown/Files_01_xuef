"""
在示例 6-1 中，每个具体策略都是一个类，而且都只定义了一个方法，
即 discount。此外，策略实例没有状态（没有实例属性）。你可能会
说，它们看起来像是普通的函数——的确如此。
"""

from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')

class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price
    def total(self):
        return self.price * self.quantity

    
class Order: # 上下文
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion
        
    def total(self): # 账面总价
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total
    
    def due(self): # 最终结算
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self) # 这里 promotion 是一个函数
            return self.total() - discount
        
    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


# 各个策略都是函数。
def fidelity_promo(order):
    """为积分为1000或以上的顾客提供5%折扣"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

def bulk_item_promo(order):
    """单个商品为20个或以上时提供10%折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

def large_order_promo(order):
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0



joe = Customer('John Doe', 0)

ann = Customer('Ann Smith', 1100)

cart = [LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)]

# 为了把折扣策略应用到 Order 实例上，只需把促销函数作为参数传入。
order1=Order(joe, cart, fidelity_promo)
# 没必要在新建订单时实例化新的促销对象，函数拿来即用。

"""
“策略对象通常是很好的享元（flyweight）。” 那本书的另一部
分对“享元”下了定义：“享元是可共享的对象，可以同时在多个上下文
中使用。” 共享是推荐的做法，这样不必在每个新的上下文（这里是
Order 实例）中使用相同的策略时不断新建具体策略对象，从而减少消
耗。
"""
# 但是，具体策略一般没有内部状态，只是处理上下文中的数据。
# 此时，一定要使用普通的函数，别去编写只有一个方法的类，再去实现另一个类声明的单函数接口。

# 函数比用户定义的类的实例轻量，而且无需使用“享元”模式，
# 因为各个策略函数在 Python编译模块时只会创建一次。
# 普通的函数也是“可共享的对象，可以同时在多个上下文中使用。

# 6.6 针对某order的最佳折扣
## promos 是函数列表。习惯函数是一等对象后，自然而然就会构建那种数据结构存储函数。
promos = [fidelity_promo, bulk_item_promo, large_order_promo]
def best_promo(order):
    return max(promo(order) for promo in promos)

# 评6.6
"""
虽然示例 6-6 可用，而且易于阅读，但是有些重复可能会导致不易察觉
的缺陷：若想添加新的促销策略，要定义相应的函数，还要记得把它添加到 promos 列表中
"""

## 扫描模块的全局符号表
##promos = [globals()[name] for name in globals()
##            if name.endswith('_promo')
##            and name != 'best_promo']

## 动态收集促销折扣函数更为显式的一种方案是使用简单的装饰器。
## 第 7章讨论函数装饰器时会使用其他方式实现这个电商“策略”模式示例。
## 使用装饰器注册可用的促销方式。


    
