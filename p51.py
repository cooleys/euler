#! /usr/bin/python

from util import *
from itertools import *

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

p = primes(10**6)
p5 = [str(i) for i in p if i > 10000 and i < 100000]
p6 = [str(i) for i in p if i > 100000 and i < 1000000]

#print len(p5) - 8000
#print len(p6) - 65000

d = {}
for i in p6:
    d_temp = {}
    for j in range(len(i)):
        if d_temp.get(i[j]) == None:
            d_temp[i[j]] = [j]
        else:
            d_temp[i[j]].append(j)
    for j in d_temp.values():
        power = list(powerset(j))[1:]
        for k in power:
            r = ''
            for l in range(len(i)):
                if l in k:
                    continue
                r += i[l]
            if d.get(r) == None:
                d[r] = {}
                d[r][k] = 1
            else:
                if d[r].get(k) == None:
                    d[r][k] = 1
                else:
                    d[r][k] += 1
for i in d.items():
    for key in i[1].keys():
        if i[1][key] == 8:
            print i[0],key
