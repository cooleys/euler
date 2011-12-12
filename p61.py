#! /usr/bin/python

# Define generators for the figurate numbers
funcs = {}
funcs[3] = lambda j: j*(j+1)/2
funcs[4] = lambda j: j**2
funcs[5] = lambda j: j*(3*j-1)/2
funcs[6] = lambda j: j*(2*j-1)
funcs[7] = lambda j: j*(5*j-3)/2
funcs[8] = lambda j: j*(3*j-2)

# Generate lists of the 4-digit figurate numbers
nums = {}
for i in range(3,9):
        j = 0
        nums[i] = []
        while True:
            n = funcs[i](j)
            if n >= 10000:
                break
            if n >= 1000:
                nums[i].append(n)
            j += 1

# Hash every number in every figurate group to corresponding numbers in the
#  other figurate groups (corresponding means that the last two digits of the
#  first number are equivalent to the first two digits of the second number)
corres = {}
for i in range(3,9):
    corres[i] = {}
    for j in range(3,9):
        if i == j:
            continue
        corres[i][j] = {}
        for num1 in nums[i]:
            for num2 in nums[j]:
                if num1 % 100 == num2 / 100:
                    if corres[i][j].get(num1) == None:
                        corres[i][j][num1] = [num2]
                    else:
                        corres[i][j][num1].append(num2)

# Perform a DFS traversal of the tree created by the mappings above, until a
#  cycle is found
def find_cycle(search_depth, prev):
    if search_depth == 5 and prev[-1][0] % 100 == prev[0][0] / 100:
        print prev
        print sum([i[0] for i in prev])
    for i in range(3,9):
        if i in [j[1] for j in prev]:
            continue
        if corres[prev[-1][1]][i].get(prev[-1][0]) != None:
            for num in corres[prev[-1][1]][i][prev[-1][0]]:
                find_cycle(search_depth + 1, prev + [(num,i)]) 

for num in nums[3]:
    find_cycle(0, [(num,3)])
