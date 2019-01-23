
##Statements
"""
Where an expression’s main job is to produce a value,
a statement’s job is to produce an effect.
Since, by definition, statements don’t evaluate to a value,
to be useful they have to otherwise change the world in some way—usually
modifying some state, reading input, or producing output.

"""

#Closures
"""
Functions are first class in Lox, which just means they are real values that
you can get a reference to, store in variables, pass around, etc.

*******************************************
fun returnFunction() {
  var outside = "outside";

  fun inner() {
    print outside;
  }

  return inner;
}

var fn = returnFunction();
fn();
*******************************************
For that to work, inner() has to “hold on” to references to any surrounding variables that
it uses so that they stay around even after the outer function has returned.
We call functions that do this “closures”. These days, the term is often used for any first-class
function, though it’s sort of a misnomer if the function doesn’t happen to close over
any variables.

As you can imagine, implementing these adds some complexity because we can no longer assume
variable scope works strictly like a stack where local variables evaporate(蒸发) the moment
the function returns.
We’re going to have a fun time learning how to make these work and do so efficiently.

"""

#Classes
"""
Since Lox has dynamic typing, lexical (roughly, “block”) scope, and closures,
it’s about halfway to being a functional language. But as you’ll see,
it’s also about halfway to being an object-oriented language.
Both paradigms have a lot going for them, so I thought it was worth covering some of each.

"""
##Why might any language want to be object oriented?
"""
In particular, for a dynamically-typed language, objects are pretty handy.
We need some way of defining compound data types to bundle blobs of stuff together.

Methods are scoped to the object, so that problem goes away.
"""

#Classes or prototypes?
"""
the basic idea is that in prototypes, you don’t need to have some “class”-like construct that
represents a “kind of thing”. Methods can exist right on an individual object and objects can
inherit from (“delegate to” in prototypal lingo) each other.

With classes, state is on the instance, but for methods, there is always a level of indirection.
When you call a method, you look up the object’s class and then you find the method there.

"""

#Classes in Lox
##syntax

##Instantiation and initialization

##Inheritance
"""
Every object-oriented language lets you not only define methods, but reuse them across
multiple classes or objects. For that, Lox supports single inheritance.
When you declare a class, you can specify a class that it inherits from using <:

class Brunch < Breakfast {
  drink() {
    print "How about a Blood Mary?";
  }
}

Here, Brunch is the derived class or subclass, and Breakfast is the base class or superclass.
Every method defined in the superclass is also available to its subclasses.

Even the init() method gets inherited. In practice, the subclass usually wants to define
its own init() method too. But the original one also needs to be called so that the superclass
can maintain its state.

As in Java, you use super for that:

class Brunch < Breakfast {
  init(meat, bread, drink) {
    super.init(meat, bread);
    this.drink = drink;
  }
}

Lox is not a pure object-oriented language.
In a true OOP language every object is an instance of a class, even primitive ones like numbers
and Booleans.

Because we don’t implement classes until well after we start working with the built-in types,
that would have been hard. So values of primitive types aren’t real objects in the sense of
being instances of classes. They don’t have methods or properties. If I were trying to make
Lox a real language for real users, I would fix that.

"""
##The Standard Library
"""
That’s the whole language, so all that’s left is the “core” or “standard” library—the set
of functionality that is implemented directly in the interpreter and that all user-defined
behavior is built on top of.


"""




























