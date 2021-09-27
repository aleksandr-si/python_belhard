def is_nengative(x):
    assert x >0

def is_odd(x):
    return x % 2 == 0

def factorization(x):
    result=[i for i in range (1,x+1) if x % i == 0 ]
    return result

def is_prime(x):
    delimiters = factorization(x)
    return len(delimiters) == 2
