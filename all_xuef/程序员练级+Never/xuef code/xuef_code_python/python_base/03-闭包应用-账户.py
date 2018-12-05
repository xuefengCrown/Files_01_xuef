"""
闭包 模拟银行账户
"""
def make_account(balance):
    def deposit(val):
        # 不考虑多线程操作
        nonlocal balance
        balance += val
        return balance
    def withdraw(val):
        nonlocal balance
        if balance < 0.01:
            return
        else:
            balance -= val
            return balance
    def ope(msg): # 存取操作的接口
        if msg == 'deposit':
            return deposit
        elif msg == 'withdraw':
            return withdraw
        else:
            raise Exception("没有这种操作!")
    return ope

# 两个独立账户
acc1 = make_account(200)
acc2 = make_account(100)

p=print
p(acc1('deposit')(800))
p(acc2('withdraw')(50))
