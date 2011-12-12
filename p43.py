#! /usr/bin/python

primes=[17,13,11,7,5,3,2]
l = []
for j in range(len(primes)):
    l.append([])
    for i in range(10,1001):
        if i % primes[j] == 0:
            i = str(i)
            if len(i) == 2:
                i = '0' + i
            if len(set(list(str(i)))) == 3:
                l[j].append(i)

d = []
for i in range(len(l)-1):
    d.append({})
    for j in l[i]:
        for k in l[i+1]:
            if str(j)[:2] == str(k)[1:]:
                if d[i].get(j) == None:
                    d[i][j] = [k]
                else:
                    d[i][j].append(k)

l2 = []
def find_nums(so_far):
    if len(so_far) == 9:
        l2.append(so_far)
        return
    if d[len(so_far)-3].get(so_far[:3]) != None:
        for next in d[len(so_far)-3][so_far[:3]]:
            test = next[0] + so_far
            if len(set(test)) == len(test):
                find_nums(test)

for key in d[0]:
    find_nums(key)

for i in range(len(l2)):
    for j in range(10):
        if str(j) not in l2[i]:
            l2[i] = str(j) + l2[i]

print sum([int(i) for i in l2])
