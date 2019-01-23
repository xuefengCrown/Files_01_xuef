
#0. Test
We've taken the tests out of their unit test frameworks and distributed them amongst
the files in python-reference/. Where unittest used calls like self.assertEqual,
we have rewritten them to ___assertEqual. We expect you to implement these predicates
as built-in checks in your implementation.

Your implementation will need to support (as built-in functions):
    ___assertTrue
    ___assertFalse
    ___assertIn
    ___assertNotIn
    ___assertEqual
    ___assertNotEqual
    ___assertRaises
    ___assertIs
    ___fail

# 3.Make sure your Python release passes all the tests:
# cd "C:\code_dxf\xuefgit\Files_01_xuef\all_xuef\程序员练级+Never\Fun_Projects\cs173-python-master"
# Racket python-main.rkt --python-path "C:\python36\python" --test-py python-reference/


# cd "C:\code_dxf\xuefgit\Files_01_xuef\all_xuef\程序员练级+Never\Fun_Projects\rython"
# Racket python-main.rkt --interp
