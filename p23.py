#! /usr/bin/python

from util import factor

factors = factor(28124)
for f in range(len(factors)):
    factors[f].remove(f)

abundant = [i for i in range(1,28124) if i < sum(factors[i])]

result = 0
for i in range(1,28124):
    print i,
    can_be = False
    for a in abundant:
        if a > (i/2):
            break
        if i - a in abundant:
            can_be = True
            break
    if not can_be:
        result += i
print result
