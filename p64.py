#! /usr/bin/python

from math import sqrt

squares = [i**2 for i in range(100)]
count = 0
for i in range(10000):
    if i in squares:
        continue
    l = [int(sqrt(i))]
    minus = l[0]
    denom = i-l[0]**2
    l.append((minus + l[0]) / denom)
    if denom == 1:
        count += 1
        continue    
    while True:
        minus = abs(minus - l[-1] * denom)
        temp = i - minus**2
        assert(temp % denom == 0)
        denom = temp/denom
        l.append((minus + l[0]) / denom)
        if denom == 1:
            if len(l) % 2 == 0:
                count += 1
            break
print count
