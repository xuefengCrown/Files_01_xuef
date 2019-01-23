
#In Python (dynamically typed), can write
class A(object):
    def f(self):
        return self.x

a1 = A(); a2 = A() # Create two As
a1.x = 3;
print a1.x # OK

# Error; there is no x
#print a2.x 


##xuef: 在 Python和 JS中，我们可以运行时编辑对象。
##鸭子类型，让类型变得宽泛了。
