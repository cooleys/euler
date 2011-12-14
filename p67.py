#! /usr/bin/python

rows = open('p67.txt','r').readlines()
rows = [[int(j) for j in i.strip().split(' ')] for i in rows]
s = [0]*101
for i in range(100):
    s = [max(s[n],s[n+1])+rows[99-i][n] for n in range(100-i)]
print s[0]
