import math
def root2(r):
    if r >=0:
        return math.sqrt(r)
    else:
        raise ValueError('Input positive number')


def root3(n):
    return n**(1/3)

