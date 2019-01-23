# A small illustration of scoping issues

class A(object):
    a1 = 12         # Instance variable

    def f1(self):
        x2 = 17                                     # a1 NOT in scope here

        def f2(b):
            while b:                                
                if h(b):
                   print x1, x2, self.a1, self.a2   # This x2 should be ...
                else:
                   x2 = 3                           # ... this one, so that
                                                    # the print statement will
                                                    # print 3 (or error)
                b = p(b,x1,x2)
        x1 = 12                                     

        f2()
        print a1        # ERROR

    a2 = a1-3                                       # OK (a1 back in scope)
