#! /usr/bin/python

# Give an ordering to the card values
ranks = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}

# Read games from file
hands = open('p54.txt', 'r').readlines()

result = 0
# Iterate through the list of games
for i in range(1000):
    winner = 2
    p = [hands[i][:14].split(' '), hands[i][15:].strip().split(' ')]
    vals = [0,0]
    kickers = [[],[]]
    # Check the value of the first player's, and then the second player's hand
    for j in [0,1]:
        r = sorted([ranks[i[0]] for i in p[j]], reverse=True)
        flush = False

        rdict = {}
        for rank in r:
            if rdict.get(rank) == None:
                rdict[rank] = 1
            else:
                rdict[rank] += 1
        rvals = sorted(rdict.values())

        # Check for pair
        if rvals == [1,1,1,2]:
            vals[j] = [k for k in rdict.keys() if rdict[k] == 2][0]
            kickers[j] = [k for k in rdict.keys() if rdict[k] != 2]

        # Check for two pair
        elif rvals == [1,2,2]:
            pairs = [k for k in rdict.keys() if rdict[k] == 2]
            vals[j] = 10000 + max(pairs) * 100 + min(pairs)
            kickers[j] = [k for k in rdict.keys() if rdict[k] != 2]

        # Check for three of a kind
        elif rvals == [1,1,3]:
            vals[j] = 20000 + [k for k in rdict.keys() if rdict[k] == 3][0]

        # Check for full house
        elif rvals == [2,3]:
            if rdict.items()[0][1] == 3:
                vals[j] = 50000 + rdict.items()[0][0]
            else:
                vals[j] = 50000 + rdict.items()[1][0]

        # Check for four of a kind
        elif rvals == [1,4]:
            if rdict.items()[0][1] == 4:
                vals[j] = 60000 + rdict.items()[0][0]
            else:
                vals[j] = 60000 + rdict.items()[1][0]

        # Check for flush
        elif len(set([k[1] for k in p[j]])) == 1:
            flush = True
            vals[j] = r[0]

        # Check for straight
        if r == range(r[0]-4, r[0]+1)[::-1]:
            vals[j] = 30000 + r[0]
        elif r == [14,5,4,3,2]:
            vals[j] = 30005

        if flush:
            vals[j] += 40000

        # Check for high card
        if vals[j] == 0:
            kickers[j] = r

    if vals[0] > vals[1]:
        result += 1
        winner = 1
    elif vals[0] == vals[1]:
        kickers[0].sort(reverse=True)
        kickers[1].sort(reverse=True)
        for i in range(len(kickers[0])):
            if kickers[0][i] != kickers[1][i]:
                if kickers[0][i] > kickers[1][i]:
                    result += 1
                    winner = 1
                break

    print p
    print vals
    print winner
    print result
    print
