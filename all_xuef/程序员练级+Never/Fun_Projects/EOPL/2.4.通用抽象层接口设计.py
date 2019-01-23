
# 构造函数 选择函数 谓词

"""
The constructors are:
    var-exp : Var → Lc-exp
    lambda-exp : Var × Lc-exp → Lc-exp
    app-exp : Lc-exp × Lc-exp → Lc-exp

The predicates are:
    var-exp? : Lc-exp → Bool
    lambda-exp? : Lc-exp → Bool
    app-exp? : Lc-exp → Bool

Finally, the extractors are:
    var-exp->var : Lc-exp → Var
    lambda-exp->bound-var : Lc-exp → Var
    lambda-exp->body : Lc-exp → Lc-exp
    app-exp->rator : Lc-exp → Lc-exp
    app-exp->rand : Lc-exp → Lc-exp
"""
#Designing an interface for a recursive data type
##1. Include one constructor for each kind of data in the data type.
##2. Include one predicate for each kind of data in the data type.
##3. Include one extractor for each piece of data passed to a constructor of the data type.
