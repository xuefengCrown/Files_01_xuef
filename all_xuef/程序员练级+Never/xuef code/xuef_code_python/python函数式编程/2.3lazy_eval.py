
0 and print("right")

#eager eval
##Other parts of Python are strict. Outside the logical operators, an expression is
##evaluated eagerly from left-to-right. A sequence of statement lines is also evaluated
##strictly in order.  Literal lists and  tuples require eager evaluation.

##When a class is created, the method functions are defined in a strict order. In the case
##of a class definition, the method functions are collected into a dictionary (by default)
##and order is not maintained after they're created. If we provide two methods with
##the same name, the second one is retained because of the strict evaluation order.
##Python's generator expressions and generator functions, however, are lazy. These
##expressions don't create all possible results immediately.
