"""
电商领域有个功能明显可以使用“策略”模式，即根据客户的属性或订单
中的商品计算折扣。
"""
# 实现 Order 类，支持插入式折扣策略
from abc import ABC, abstractmethod # Abstract Base Class
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity') # fidelity 积分

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
            discount = self.promotion.discount(self)
            return self.total() - discount
        
    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC) : # 策略：抽象基类
    @abstractmethod
    def discount(self, order):
        """返回折扣金额（正值）"""


class FidelityPromo(Promotion): # 第一个具体策略
    """为积分为1000或以上的顾客提供5%折扣"""
    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion): # 第二个具体策略
    """单个商品为20个或以上时提供10%折扣"""
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount


class LargeOrderPromo(Promotion): # 第三个具体策略
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0

    
joe = Customer('John Doe', 0) 
ann = Customer('Ann Smith', 1100)

cart = [LineItem('banana', 4, .5), 
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)]

order1=Order(joe, cart, FidelityPromo()) # <Order total: 42.00 due: 42.00>

order2=Order(ann, cart, FidelityPromo()) # <Order total: 42.00 due: 39.90>

p=print
p(order1)
p(order2)


