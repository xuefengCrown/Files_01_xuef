
#Chapter 1: Computing with Text
"""
One way of defining a language is to write prose paragraphs that explain the kinds of
expressions that are allowed in the language and how they are evaluated.

Another way of defining a language is to implement an interpreter for it in some meta-
language.
The meta-language used to define another language need not execute efficiently, since its
primary purpose is to explain the other language to humans.

The meta-language’s primitive data constructs need not be defined in terms of bits and bytes.


"""
##formal analysis
##meta-language???


##1.1 Defining Sets
####When we write a BNF grammar, such as
"""
B = t
  | f
   | (B • B)

then we actually define a set B of textual strings.
The above definition can be expanded to the following constraints on B:
            t ∈ B
            f ∈ B
    a ∈ B and b ∈ B ⇒ (a • b) ∈ B
Technically, the set B that we mean is the smallest set that obeys the above constraints.

set B is defined recursively.
 
"""



#Chapter2  Structural Induction
"""
P = α
| (β⊗P)
| (P?P)

Theorem 2.1: For any P, P contains an equal number of βs and ⊗s.

Proof for Theorem 2.1: By induction on the structure of P.
• Base cases:
– Case α
α contains 0 βs and 0 ⊗s, so the claim holds.
• Inductive cases:
– Case (β⊗P)
By induction, since P is a substructure of (β⊗P), P contains an equal
number—say, n—of βs and ⊗s. Therefore, (β⊗P) contains n + 1 βs and
⊗s, and the claim holds.
– Case (P 1 ?P 2 )
By induction, P 1 contains an equal number—say, n 1 —of βs and ⊗s. Sim-
ilarly, P 2 contains n 2 βs and ⊗s. Therefore, (P 1 ?P 2 ) contains n 1 + n 2 βs
and ⊗s, and the claim holds.

"""
##structural induction???




##

"""
adopt a couple of conventions for dropping parentheses, plus one for dropping λs:
• Application associates to the left: M1 M2 M3 means ((M1 M2) M3)
• Application is stronger than abstraction: λX. M1 M2 means (λX.(M1 M2))
• Consecutive lambdas can be collapsed: λXYZ.M means (λX.(λY.(λZ.M)))

"""
