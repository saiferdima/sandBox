


from math import *


def primes():
    x = 2
    if (((factorial(x - 1)) + 1) % x == 0):
        yield (x)
    x += 1