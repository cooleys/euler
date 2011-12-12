#! /usr/bin/python

from util import primes
from util import inb
p = primes(1000000)

s = []
res = 21
for i in range(len(p)):
    s.append(sum(p[i:i+res]))
    if s[i] > 1000000:
        break

while s != []:
    res += 2
    for i in range(len(s)):
        s[i] += p[i+res-1] + p[i+res-2]
        if s[i] > 1000000:
            s = s[:i]
            break
        if inb(s[i],p):
            print s[i],res
