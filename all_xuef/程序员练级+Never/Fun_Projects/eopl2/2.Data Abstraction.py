
#2.1 Specifying Data via Interfaces
"""
Every time we decide to represent a certain set of quantities in a particular
way, we are defining a new data type: the data type whose values are those
representations and whose operations are the procedures that manipulate
those entities.
"""
##数据抽象的好处
##1. 隐藏内部表示细节
##2. 方便以后改变数据表示

#接口与实现
#Data abstraction divides a data type into two pieces: an interface and an implementation.


#constructors, extractors, predicates
"""
Designing an interface for a recursive data type
1. Include one constructor for each kind of data in the data type.
2. Include one predicate for each kind of data in the data type.
3. Include one extractor for each piece of data passed to a constructor
of the data type.
"""

#2.4 A Tool for Defining Recursive Data Types
"""
For complicated data types, applying the recipe for constructing an interface
can quickly become tedious. In this section, we introduce a tool for automatically
constructing and implementing such interfaces in Scheme.


a define-datatype declaration has the form
(define-datatype type-name type-predicate-name
    {(variant-name { (field-name predicate) }∗ )}+ )

Thiscreatesadatatype, namedtype-name, withsome variants.
Each variant has avariant-nameand zeroor more fields, each with its own field-name and
associated predicate.

The type-predicate-name is bound to a predicate. This predicate determines
if its argument is a value belonging to the named type.
"""
##类型与变种
##类型谓词与各变种的域选择器会自动生成

#非常适合定义结构递归的数据

#命名习惯(约定)
"""
S-list :: = ( {S-exp}∗ )
 S-exp :: = Symbol | S-list

(define-datatype s-list s-list?
  (empty-s-list)
  (non-empty-s-list
   (first s-exp?)
   (rest s-list?)))
(define-datatype s-exp s-exp?
  (symbol-s-exp
   (sym symbol?))
  (s-list-s-exp
   (slst s-list?)))

"""

#具体语法与抽象语法!!!
"""
In the abstract syntax, terminals such as parentheses need not be stored,
because they convey no information.
On the other hand, we want to make sure that the data structure allows us to
determine what kind of lambda-calculus expression it represents,
and to extract its components.
"""
#字符串是无结构的，杂乱的信息。但是，因为它是被语法约束的，所以我们能够将其转化为
#结构化的数据。(such as tree)
"""
concrete syntax, which is primarily useful for humans,
and abstract syntax, which is primarily useful for computers.
"""




