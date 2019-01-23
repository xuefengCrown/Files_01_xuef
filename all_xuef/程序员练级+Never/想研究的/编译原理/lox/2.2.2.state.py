# now we work on state

##Global Variables
"""
1. A variable declaration statement brings a new variable into the world:
  var beverage = "espresso";
This creates a new binding that associates a name (here “beverage”) with a
value (here, the string "espresso").

2. Once that’s done, a variable expression accesses that binding.
  print beverage;
"""

##comments on global state
"""
Global state gets a bad rap. Sure, lots of global state—especially mutable state—
makes it hard to maintain large programs. It’s good software engineering to minimize
how much you use.
"""

##statement 不是可以出现在任何位置的!

## 扩展语法
"""
program     → declaration* EOF ;

declaration → varDecl
            | statement ;

statement   → exprStmt
            | printStmt ;

varDecl → "var" IDENTIFIER ( "=" expression )? ";" ;

//To access a variable, we define a new kind of primary expression:
primary → "true" | "false" | "nil" | "this"
        | NUMBER | STRING
        | "(" expression ")"
        | IDENTIFIER ;
        
Declaration statements go under the new declaration rule. Right now, it’s only variables,
but later it will include functions and classes. Any place where a declaration is allowed
also allows non-declaring statements, so the declaration rule falls through to statement.
"""

##函数定义和类定义也是声明的一种，就像变量声明！


##where variables live in memory???
###Environments

##lookup
"""
If the variable is found, it simply returns the value bound to it.
But what if it’s not? Again, we have a choice.
1. Make it a syntax error.
2. Make it a runtime error.
3. Allow it and return some default value like nil.

The problem is that using a variable isn’t the same as referring to it.
You can refer to a variable in a chunk of code without immediately evaluating it
if that chunk of code is wrapped inside a function. If we make it a static error to
mention a variable before it’s been declared, it becomes much harder to define
recursive functions.

Since making it a static error makes recursive declarations too difficult,
we’ll defer the error to runtime. It’s OK to refer to a variable before it’s defined
as long as you don’t evaluate the reference.
"""
##互递归(lookup实现)
"""
Some statically-typed languages like Java and C# solve this by specifying that
the top level of a program isn’t a sequence of imperative statements.
Instead, a program is a set of declarations which all come into being simultaneously.
The implementation declares all of the names before looking at the bodies of any of
the functions.

Older languages like C and Pascal don’t work like this. Instead, they force you to
add explicit forward declarations to declare a name before it’s fully defined.
That was a concession(让步) to the limited computing power at the time. They wanted to be able
to compile a source file in one single pass through the text, so those compilers couldn’t
gather up all of the declarations first before processing function bodies.
"""

##Assignment
##解析
"""
expression → assignment ;
assignment → IDENTIFIER "=" assignment
           | equality ;

Here is where it gets tricky. A single token lookahead recursive descent parser can’t see
far enough to tell that it’s parsing an assignment until after it has gone through the
left-hand side and stumbled onto the =. You might wonder why it even needs to.
After all, we don’t know we’re parsing a + expression until after we’ve finished
parsing the left operand.
"""
##l-value
"""
An l-value “evaluates” to a storage location that you can assign into.

Because an l-value isn’t evaluated like a normal expression, the syntax tree must reflect that.
That’s why the Expr.Assign node has a Token for the left-hand side, not an Expr.
The problem is that the parser doesn’t know it’s parsing an l-value until it hits the =.

"""
##assignment 示例
"""
newPoint(x + 2, 0).y = 3;
obj.field = a;
"""


##local variable
"""
We want local variables, which means it’s time for scope.
"""
###Scope
"""
Lexical scope (“static scope”) is a specific style of scope where
the text of the program itself shows where a scope begins and ends.

When you see an expression that uses some variable, you can figure out
which variable declaration it refers to just by statically reading the code.

Lox doesn’t have dynamically scoped variables, but methods and fields on objects
are dynamically scoped:

class Saxophone {
  play() {
    print "Careless Whisper";
  }
}

class GolfClub {
  play() {
    print "Fore!";
  }
}

fun playIt(thing) {
  thing.play();
}
"""

###syntax(C-ish like)
"""
{
  var a = "in block";
}
print a; // Error! No more "a".

The beginning of a block introduces a new local scope, and that scope ends
when execution passes the closing }. Any variables declared inside the block disappear.
"""

###Nesting and shadowing
"""
When a local variable has the same name as a variable in an enclosing scope,
it shadows the outer one.

In order to find them, the interpreter must search not only the current innermost
environment, but also any enclosing ones.

::= env chain
"""

###Block syntax and semantics
####the grammar:
"""
statement → exprStmt
          | printStmt
          | block ;

block     → "{" declaration* "}" ;

A block is itself a statement and can appear anywhere a statement is allowed.
"""

### newEnv
"""
Explicitly changing and restoring a mutable environment field may seem a little inelegant.
Another classic approach is to explicitly pass the environment as a parameter to each
visit method. To “change” the enviroment, you pass a different one as you recurse down
the tree. You don’t have to restore the old one, since the new one lives on the Java stack
and is implicitly discarded when the interpreter returns from the block’s visit method.

I considered that for jlox, but it’s kind of tedious and verbose adding an environment
parameter to every single visit method.
"""






























