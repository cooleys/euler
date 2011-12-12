#! /usr/bin/python

max = 0
for i in range(1,100):
    for j in range(1,100):
        s = sum([int(k) for k in list(str(i**j))])
        if s > max:
            max = s
print max
