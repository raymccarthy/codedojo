# import decimal

# def pi():
#     """
#     Compute Pi to the current precision.

#     Examples
#     --------
#     >>> print(pi())
#     3.141592653589793238462643383

#     Notes
#     -----
#     Taken from https://docs.python.org/3/library/decimal.html#recipes
#     """
#     decimal.getcontext().prec += 2  # extra digits for intermediate steps
#     three = decimal.Decimal(3)      # substitute "three=3.0" for regular floats
#     lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
#     while s != lasts:
#         lasts = s
#         n, na = n + na, na + 8
#         d, da = d + da, da + 32
#         t = (t * n) / d
#         s += t
#     decimal.getcontext().prec -= 2
#     return +s               # unary plus applies the new precision

# decimal.getcontext().prec = 10000
# pi = pi()
# print(pi)

import math 
import decimal

i = 0

sum = decimal.Decimal(0) 

calc = decimal.Decimal(0) 

a = decimal.Decimal(0) 
b1 = decimal.Decimal(0) 
c1 = decimal.Decimal(0) 
d1 = decimal.Decimal(0) 
e1 = decimal.Decimal(0) 



for i in range(0,1000):
    a = decimal.Decimal(1) / (16 ** i)
    b1 = decimal.Decimal(4) / (8 * i + 1)
    c1 = decimal.Decimal(2)/ (8 * i + 4)
    d1 = decimal.Decimal(1) / (8 * i + 5)
    e1 = decimal.Decimal(1) / (8 * i + 6)     
    
    calc = a * (b1 - c1 - d1 - e1)

    sum = sum + calc
    
    print(sum)