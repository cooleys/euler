lines = open('p96.out','r').readlines()
lines = [line.strip() for line in lines]
sudokus = [lines[i*10:i*10+9] for i in range(len(lines))]
digits = [str(i) for i in range(1,10)]
for i in range(len(sudokus)):
    is_sol = True
    for j in range(9):
        if sorted(sudokus[i][j]) != digits:
            print '1'
            print j
            print sorted(sudokus[i][j])
            is_sol = False
        if sorted([sudokus[i][k][j] for k in range(9)]) != digits:
            print '2'
            print j
            print sorted([sudokus[i][k][j] for k in range(9)])
            #print sudokus[i]
            is_sol = False
        if sorted(sudokus[i][j/3*3+k%3][j%3*3+k/3] for k in range(9)) != digits:
            print '3'
            print j
            print sorted(sudokus[i][j/3*3+k%3][j%3*3+k/3] for k in range(9))
            is_sol = False
    if is_sol:
        print 'Sudoku %d solution is valid' % i
    else:
        print 'Sudoku %d solution is bad!' % i
