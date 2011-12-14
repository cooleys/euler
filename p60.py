#! /usr/bin/python

from util import *

p = primes(1000000)



'''
p4 = []
for i in p:
    if i > 10000:
        break
    p4.append(i)

l = []
for i in range(len(p4)-1):
    for j in range(i+1, len(p4)):
        temp1 = int(str(i) + str(j))
        temp2 = int(str(j) + str(i))
        if temp1 < 1000000:
            if not inb(temp1, p) or not inb(temp2, p):
                continue
            l.append([i,j])
        else:
            if not is_prime(temp1, p) or not is_prime(temp2, p):
                continue
            l.append([i,j])
print l
print len(p4)
print len(l)
'''
