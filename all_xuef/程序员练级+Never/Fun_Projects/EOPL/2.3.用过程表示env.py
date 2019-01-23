# env 的Procedural Representation(过程性表示)很有启发性
"""
(define empty-env
    (lambda ()
        (lambda (search-var)
           (report-no-binding-found search-var))))

(define extend-env
    (lambda (saved-var saved-val saved-env)
        (lambda (search-var)
            (if (eqv? search-var saved-var)
                saved-val
                (apply-env saved-env search-var)))))

(define apply-env
    (lambda (env search-var)
        (env search-var)))
"""
# 下面我用python来表述
def empty_env(): #empty_env===你什么都search不到的set
    def inner(search_var):
        raise Exception("no-binding-found for var:", search_var)
    return inner

#The procedure extend-env returns a new procedure that represents the extended environment.
def extend_env(saved_var, saved_val, p_env):
    def inner(search_var):
        if search_var == saved_var:
            print("Got: ", search_var, "==", saved_val)
            return saved_val
        else:
            print("Search further...")
            return apply_env(p_env, search_var) # search in parent env
    return inner
def apply_env(env, search_var): # env is a procedure
    return env(search_var)

empty_e = empty_env()
#print(empty_e("x"))

env = extend_env('d', 4,
                  extend_env('c', 3,
                             extend_env('b', 2,
                                        extend_env('a', 1, empty_e))))

print(env)
print(apply_env(env, 'b'))






