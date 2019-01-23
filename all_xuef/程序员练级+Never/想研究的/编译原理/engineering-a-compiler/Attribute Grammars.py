
#Attribute Grammars
"""
They give a formal way to pass semantic information (types, values, etc.) around a parse tree.


In other words, synthesized attributes get their values from their children
while inherited attributes get their values from their parent and siblings.


In the E ::= E+T example a from a few slides ago
the attributes are all synthesized -- passed from the leaves up;
evaluation of such attributes can be done easily in a bottom-up pass through the tree.


Here is an example that uses attributes for
automatic type evaluation. The st attribute is a
symbol table -- a list of (id,type) pairs.
(L1===L, S1===S)

S ::= DEC {S.st = DEC.st}
S ::= S1 DEC {S.st = S1.st || DEC.st} (||=concatenate)
DEC ::= T L ; {L.type = T.type; DEC.st = L.st}
T ::= int {T.type = int}
T ::= string {T.type = string}
L ::= id {L.st = (id.name, L.type)}
L ::= L1, id {L1.type = L.type; L.st = L1.st || (id.name, L.type)}

Note that L.type is inherited, but the st attribute is synthesized.

int a, b, c;
string s;
"""

# L-attributed grammar???

















