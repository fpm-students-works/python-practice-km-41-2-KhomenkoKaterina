a = int(input('Insert a number: '))
def fact(a):
    if a == 0:
        return 1
    else:
        return a * fact(a-1)
print('Factorial: ', fact(a))
fact(a)