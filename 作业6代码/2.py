def zero(fun=None): 
    return fun(0) if fun else 0
def one(fun=None): 
    return fun(1) if fun else 1
def two(fun=None): 
    return fun(2) if fun else 2
def three(fun=None): 
    return fun(3) if fun else 3
def four(fun=None): 
    return fun(4) if fun else 4
def five(fun=None):
    return fun(5) if fun else 5
def six(fun=None): 
    return fun(6) if fun else 6
def seven(fun=None): 
    return fun(7) if fun else 7
def eight(fun=None): 
    return fun(8) if fun else 8
def nine(fun=None): 
    return fun(9) if fun else 9

def plus(y): 
    return lambda x: x + y
def minus(y): 
    return lambda x: x - y
def times(y): 
    return lambda x: x * y
def divided_by(y): 
    return lambda x: x // y 
