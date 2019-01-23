
#Listing 4.10: A simple descriptor for type checking attribute values
class TypedAttribute:
    
    def __init__(self, name, type, default=None):
        self.name = "_" + name
        self.type = type
        self.default = default if default else type()

    def __get__(self, instance, cls):
        return getattr(instance, self.name, self.default)

    def __set__(self,instance,value):
        if not isinstance(value,self.type):
            raise TypeError("Must be a %s" % self.type) 
        setattr(instance,self.name,value)
    
    def __delete__(self,instance):
        raise AttributeError("Can't delete attribute")

class Account:
    name = TypedAttribute("name",str) 
    balance = TypedAttribute("balance",int, 42)
    
    def name_balance_str(self):
        return str(self.name) + str(self.balance)

acc1 = Account()
acc2 = Account()
acc1.name = "xuef"

print(acc1.name_balance_str())
print(acc2.name_balance_str())
