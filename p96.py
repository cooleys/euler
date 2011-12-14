#! /usr/bin/python

from os import system
from itertools import product
from copy import deepcopy as d

lines = open('p96.txt','r').readlines()
sudokus = [lines[i*10+1:i*10+10] for i in range(len(lines)/10)]
sudokus = [[[int(i) for i in list(i.strip())] for i in sudoku] for sudoku in sudokus]

def display(s):
    #system('clear')
    for line in s:
        print ' '.join([str(i) for i in line])
        print
    print
    raw_input()

def solve(s, n):
    if n == 81:
        return s
    for r,c in list(product(range(9), range(9))):
        if s[r][c] == 0:
            break

    row = s[r]
    col = [s[i][c] for i in range(9)]
    box = [[s[i+r/3*3][j+c/3*3] for i in range(3)] for j in range(3)]
    box = box[0]+box[1]+box[2]
    remain = [i for i in range(1,10) if i not in row+col+box]
    for i in remain:
        s[r][c] = i
        a = solve(d(s), n+1)
        if a != None:
            return a
 

#for i in range(len(sudokus)):
result = 0
for i in range(50):
    print i
    temp = ([[j for j in line if j != 0] for line in sudokus[i]])
    nonzero = sum([len(j) for j in temp])
    s = solve(d(sudokus[i]), nonzero)
    result += int(''.join([str(s[0][i]) for i in range(3)]))
print result
