  
tolerance = 0.1
def fixed_point(f, first_guess):
    def close_enough(x1, x2):
        return abs(x1-x2)<tolerance
    
    def try_guess(guess):
        next_ = f(guess)
        if close_enough(guess, next_):
            return next_
        
        return try_guess(next_)
    
    return try_guess(first_guess)

def mySqrt(x):
    return fixed_point(lambda y:0.5*(y+x/y), 1.0)

print(mySqrt(9))
