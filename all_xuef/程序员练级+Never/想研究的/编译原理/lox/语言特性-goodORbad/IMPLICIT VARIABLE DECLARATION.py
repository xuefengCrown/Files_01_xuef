
#IMPLICIT VARIABLE DECLARATION
"""
Lox has distinct syntax for declaring a new variable and assigning to an existing one.
Some languages collapse those to only assignment syntax. Assigning to a non-existent
variable automatically brings it into being. This is called implicit variable declaration
and exists in Python, Ruby.

When the same syntax can assign or create a variable, each language must decide what happens
when it isn’t clear about which behavior the user intends. In particular, each language must
choose how implicit declaration interacts with shadowing, and which scope an implicitly
declared variable goes into.
"""
##python
"""
In Python, assignment always creates a variable in the current function’s scope,
even if there is a variable with the same name declared outside of the function.
"""

##js
"""
In JavaScript, assignment modifies an existing variable in any enclosing scope, if found.
If not, it implicitly creates a new variable in the global scope.
"""


## Implicit declaration has some problems.
"""
1.A user may intend to assign to an existing variable, but may have misspelled it.

3.In Python, you may want to assign to some variable outside of the current function
instead of creating a new variable in the current one, but you can’t.


Over time, the languages I know with implicit variable declaration ended up adding
more features and complexity to deal with these problems.

1.Implicit declaration of global variables in JavaScript is universally considered a
mistake today. “Strict mode” disables it and makes it a compile error.

2.Python added a global statement to let you explicitly assign to a global variable
from within a function. Later, as a functional programming style and nested functions
became more popular, they added a similar nonlocal statement to assign to variables
in enclosing functions.

My opinion is that implicit declaration made sense in years past when most scripting
languages were heavily imperative and code was pretty flat. As programmers got more
comfortable with deep nesting, functional programming, and closures, it’s become
much more common to want access to variables in outer scopes. That makes it more
likely that users will run into the tricky cases where it’s not clear whether they
intend their assignment to create a new variable or reuse a surrounding one.

So I prefer explicitly declaring variables, which is why Lox requires it.
"""














