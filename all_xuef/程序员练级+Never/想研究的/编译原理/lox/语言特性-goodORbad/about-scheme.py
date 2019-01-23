
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


Some languages make this split explicit. In Scheme and ML, when you declare a local variable
using let, you also delineate the subsequent code where the new variable is in scope.
There is no implicit “rest of the block”.
"""
