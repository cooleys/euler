#! /usr/bin/python

from math import sqrt
from util import cf_denom

xs = {}
for i in range(2,1001):
    if int(sqrt(i)) == sqrt(i):
        continue
    denoms = cf_denom(i)
    A_0 = 1
    A = denoms[0]
    B_0 = 0
    B = 1
    j = 1
    while True:
        if A**2 - i*B**2 == 1: 
            xs[i] = A
            break
        A_0, A = A, denoms[j]*A + A_0
        B_0, B = B, denoms[j]*B + B_0
        j += 1
        if j == len(denoms):
            j = 1
print max(xs.items(), key=(lambda x: x[1]))
