
#Function Calls
"""
the callee—can be any expression that evaluates to a function.

This “operator” has higher precedence than any other operator, even the unary ones. 
"""
##syntax
"""
unary → ( "!" | "-" ) unary | call ;
call  → primary ( "(" arguments? ")" )* ;
arguments → expression ( "," expression )* ;
"""

##argument求值顺序
"""
Since argument expressions may have side effects, the order they are evaluated
may be user visible. Even so, some languages like Scheme and C don’t specify an order.
This gives compilers freedom to reorder them for efficiency, but means users may be
unpleasantly surprised if arguments aren’t evaluated in the order they expect.
"""
##错误处理
###1.callee object 是否可调用???
###2.参数个数是否匹配???
###3.参数类型是否兼容???

#我们的实现的运行时环境，包括哪些东西?
##primitive procedures

##命名空间
"""
In Lox, functions and variables occupy the same namespace.
In Common Lisp, the two live in their own worlds. A function and variable with the same name
don’t collide. If you call the name, it looks up the function. If you refer to it, it looks up
the variable. This does requires jumping through some hoops when you do want to refer
to a function as a first-class value.

languages like Scheme that put functions and variables in the same namespace.
"""

##Function Declarations
"""
Function declarations, like variables, bind a new name.
That means they are only allowed in places where a declaration is permitted.

declaration → funDecl
            | varDecl
            | statement ;
    That references this new rule:
funDecl  → "fun" function ;
function → IDENTIFIER "(" parameters? ")" block ;

parameters → IDENTIFIER ( "," IDENTIFIER )* ;

It’s like the earlier arguments rule, except that
each parameter is an identifier, not an expression. 
"""
##函数定义意味什么
"""
A named function declaration isn’t really a single primitive operation.
It’s syntactic sugar for two distinct steps:
(1) creating a new function object and
(2) binding a new variable to it. If Lox had syntax for anonymous functions,
we wouldn’t need function declaration statements. You could just do:

var add = fun (a, b) {
  print a + b;
};
"""
###如何 represent a function???
"""
在《怎样写个解释器》中，王垠使用 Closure(lambda-exp, saved-env)来表示;
让我印象深刻的是——他使用了(定义中的)完整的 lambda表达式
其实也只是保存 params && body，只不过他不想手动parse，而是想在函数调用时使用
racket的模式匹配来帮助解析出 params && body。

关于函数的类型，王也有自己的看法: 一个函数的类型就是它自己。
"""
##Function Objects
"""
We’ve got some syntax parsed so usually we’re ready to interpret, but first
we need to think about how to represent a Lox function in Java.

We need to keep track of the parameters so that we can bind them to argument values
when the function is called. And, of course, we need to keep around the code for the
body of the function so that we can execute it.

We also need a class that implements LoxCallable so that we can call it.
We don’t want the runtime phase of the interpreter to bleed into the front-end’s syntax
classes so we don’t want Stmt.Function itself to implement that.
Instead, we wrap it in a new class.
"""
##core of function
"""
Core to functions are the idea of parameters, and that a function encapsulates
those parameters—no other code outside of the function can see them.
This means each function gets its own environment where it stores those variables.

Further, this environment must be created dynamically. Each function call gets its
own environment. Otherwise, recursion would break. If there are multiple calls to
the same function in play at the same time, each needs its own environment, even though
they are all calls to the same function.
"""

##Return Statements
"""
We can get data into functions by passing parameters, but we’ve got no way to get
results back out. If Lox was an expression-oriented language like Ruby or Scheme,
the body would be an expression whose value is implicitly the function’s result.
But in Lox, the body of a function is a list of statements which don’t produce values,
so we need dedicated syntax for emitting a result. In other words, return statements.

The Hotel California of data.

statement  → exprStmt
           | forStmt
           | ifStmt
           | printStmt
           | returnStmt
           | whileStmt
           | block ;

returnStmt → "return" expression? ";" ;

"""
##Returning from calls
"""
Interpreting a return statement is tricky. You can return from anywhere within the body
of a function, even deeply nested inside other statements.
"""

##Local Functions and Closures
"""
This is the environment that is active when the function is declared not when it’s called,
which is what we want. It represents the lexical scope surrounding the function declaration.

With closures, we can abstract and compose data.

This may be surprising, but you can use a closure to represent arbitrary data structures
(though the resulting code does look kind of funny).
Since a closure contains an environment—a Java Map in our implementation—it is a
data structure.

Of course, we will add more natural support for first-class data structures when we add classes.
But even now, it’s possible to define a function that works like an object.
Cogitate on this:

fun makePoint(x, y) {
  fun closure(method) {
    if (method == "x") return x;
    if (method == "y") return y;
    print "unknown method " + method;
  }

  return closure;
}

var point = makePoint(2, 3);
print point("x"); // "2".
print point("y"); // "3".
"""

##???
"""
var a = "global";
{
  fun showA() {
    print a;
  }

  showA();
  var a = "block";
  showA();
}

If you’re familiar with closures in other languages, you’ll
expect it to print “global” twice.
"""
##A block is not all actually the same scope.
"""
Consider:

{
  var a;
  // 1.
  var b;
  // 2.
}
At the first marked line, only a is in scope. At the second line, both a and b are.
If you define a “scope” to be a set of declarations, then those are clearly not
the same scope—they don’t contain the same declarations. It’s like each variable
statement splits the block into two separate scopes, the scope before the variable
is declared and the one after, which includes the new variable.
"""
##But in our implementation, environments do act like the entire block is one scope,
##just a scope that changes over time.
"""
Closures do not like that. When a function is declared, it captures a reference to
the current environment. The function should capture a frozen snapshot of the environment
as it existed at the moment the function was declared. But, instead, in the Java code,
it has a reference to the actual mutable environment object. When a variable is later
declared in the scope that environment corresponds to, the closure sees the new variable,
even though the declaration does not precede the function.
"""
###Persistent environments
"""
a persistent data structure can never be directly modified.
Instead, any “modification” to an existing structure produces a brand new object
that contains all of the original data and the new modification.
The original is left unchanged.

This sounds like it might waste tons of memory and time copying the structure each time.
In practice, persistent data structures share most of their data between the different
“copies”.

If we were to apply that technique to Environment, then every time you declared a variable
it would return a new environment that contained all of the previously-declared variables
along with the one new name. Declaring a variable would do the implicit “split” where
you have an environment before the variable is declared and one after.


A closure retains a reference to the Environment instance in play when the function was declared.
Since any later declarations in that block would produce new Environment objects, the closure
wouldn’t see the new variables and our bug would be fixed.

This is a legit way to solve the problem, and it’s the classic way to implement environments
in Scheme interpreters. We could do that for Lox, but it would mean going back and changing
a pile of existing code.
"""

##Semantic Analysis
"""
We know static scope means that a variable usage always resolves to the same declaration,
which can be determined just by looking at the text.

A better solution is to resolve each variable use once. Write a chunk of code that inspects
the user’s program, finds every variable mentioned, and figures out which declaration each
refers to. This process is an example of a semantic analysis.

Where a parser only tells if a program is grammatically correct—a syntactic analysis—
semantic analysis goes farther and starts to figure out what pieces of the program
actually mean.

In this case, our analysis will resolve variable bindings. We’ll know not just that
an expression is a variable, but which variable it is.
"""

##A variable resolution pass
"""
After the parser produces the syntax tree, but before the interpreter starts executing it,
we’ll do a single walk over the tree to resolve all of the variables it contains.
Additional passes between parsing and execution are common. If Lox had static types,
we could slide a type checker in there. Optimizations are often implemented in separate
passes like this too. Basically, any work that doesn’t rely on state that’s only available
at runtime can be done in this way.

Our variable resolution pass works like a sort of mini-interpreter. It walks the tree,
visiting each node, but a static analysis is different from a dynamic execution.


Only a couple of nodes are interesting when it comes to resolving variables:

1.A block statement introduces a new scope for the statements it contains.

2.A function declaration introduces a new scope for its body and binds its parameters
in that scope.

3.A variable declaration adds a new variable to the current scope.

4.Variable and assignment expressions need to have their variables resolved.
"""

##Interpreting Resolved Variables
"""
Let’s see what our resolver is good for. Each time it visits a variable,
it tells the interpreter how many scopes there are between the current scope
and the scope where the variable is defined. At runtime, this corresponds exactly
to the number of environments between the current one and the enclosing one where
the interpreter can find the variable’s value.

We want to store the resolution information somewhere so we can use it when the variable
or assignment expression is later executed, but where? One obvious place is right in the
syntax tree node itself. That’s a fine approach, and that’s where many compilers store
the results of analyses like this.

"""








































