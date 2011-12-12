#! /usr/bin/python

word_list = open('words.txt','r').read().split(' ')
message = open('p59.txt','r').read().split(',')

for i in range(97,123):
    for j in range(97,123):
        for k in range(97,123):
            key = [i,j,k] * 400 + [i]
            decr = ''.join([chr(key[x]^int(message[x])) for x in range(len(message))])
            """
            correct = True
            for w in ''.join(i for i in decr if (ord(i) > 96 and ord(i) < 123) or i == ' ').split(' '):
                if w not in word_list:
                    correct = False
                    break
            if correct:
            """
            if len([l for l in decr if l == ' ']) > 100 and decr.find('Gospel') != -1:
                print decr
                print sum([ord(x) for x in decr])
