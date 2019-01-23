
#变量可以 后声明先使用
"""
In JavaScript, variables declared using var are implicitly “hoisted” to(升起)
the beginning of the block. Any use of that name in the block will refer to that variable,
even if the use appears before the declaration. When you write this in JavaScript:

{
  console.log(a);
  var a = "value";
}
It behaves like:

{
  var a; // Hoist.
  console.log(a);
  a = "value";
}
That means that in some cases you can read a variable before its initializer
has run—an annoying source of bugs.
"""
