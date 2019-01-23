

#Listing 3.0: A cross section of the Python BNF Grammar
"""
 1         stmt: simple_stmt | compound_stmt
 2         simple_stmt: small_stmt (';' small_stmt)* [';'] NEWLINE
 3         small_stmt: (expr_stmt | del_stmt | pass_stmt | flow_stmt |
 4                 import_stmt | global_stmt | nonlocal_stmt | assert_stmt)
 5         expr_stmt: testlist_star_expr (augassign (yield_expr|testlist) |
 6                         ('=' (yield_expr|testlist_star_expr))*)
 7         testlist_star_expr: (test|star_expr) (',' (test|star_expr))* [',']
 8         augassign: ('+=' | '-=' | '*=' | '@=' | '/=' | '%=' | '&=' | '|=' | '^=' 
 9                 | '<<=' | '>>=' | '**=' | '//=')
10 
11         del_stmt: 'del' exprlist
12         pass_stmt: 'pass'
13         flow_stmt: break_stmt | continue_stmt | return_stmt | raise_stmt | 
14                 yield_stmt
15         break_stmt: 'break'
16         continue_stmt: 'continue'
17         return_stmt: 'return' [testlist]
18         yield_stmt: yield_expr
19         raise_stmt: 'raise' [test ['from' test]]
20         import_stmt: import_name | import_from
21         import_name: 'import' dotted_as_names
22         import_from: ('from' (('.' | '...')* dotted_name | ('.' | '...')+)
23                 'import' ('*' | '(' import_as_names ')' | import_as_names))
24         import_as_name: NAME ['as' NAME]
25         dotted_as_name: dotted_name ['as' NAME]
26         import_as_names: import_as_name (',' import_as_name)* [',']
27         dotted_as_names: dotted_as_name (',' dotted_as_name)*
28         dotted_name: NAME ('.' NAME)*
29         global_stmt: 'global' NAME (',' NAME)*
30         nonlocal_stmt: 'nonlocal' NAME (',' NAME)*
31         assert_stmt: 'assert' test [',' test]
32 
33         ...
"""
