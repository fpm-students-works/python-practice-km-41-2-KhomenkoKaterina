import math
def log(a, b):
    if a>0 and a != 1 and b>0:
        return math.log(b, a)
    else:
        print('Input correct number')

def ln(b):
    if b > 1:
        return math.log(b, math.e)
    else:
        print('Input correct number')

def lg(b):
    if b>0:
        return math.log10(b)
    else:
        print('Input correct number')





