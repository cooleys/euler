#! /usr/bin/python

vals = [[1,2*(33-i),1] for i in range(33)]
vals = [a for b in vals for a in b] + [2]

n,d = 1,0
for i in vals:
    n,d = d,n
    n += d*i

print sum([int(i) for i in list(str(n))])
