## source link

https://en.wikipedia.org/wiki/Breadth-first_search#Applications

https://stackoverflow.com/questions/23083203/what-is-common-applications-for-level-order-traversal-in-binary-tree



## Traversal

### preorder



### inorder



### postorder



### level-order

实际上是一种 bfs（[Level order traversal](http://en.wikipedia.org/wiki/Tree_traversal#Queue-based_level_order_traversal) is actually a [BFS](http://en.wikipedia.org/wiki/Breadth-first_search)）

So , to find nodes at a distance `X` units from a given `node` , you **don't need to travel full graph**(which can be very large ) , but just need to traverse all `nodes` at distance `<=X` , consider the case when `X` is very small compared to `height` of tree .







