from math import sqrt

# Generate primes up to n by trial division
def primes(n, show=False):
        primes = [2]
        for i in range(3,n,2):
            is_prime = True
            for prime in primes:
                if prime > sqrt(i):
                    break
                elif i % prime == 0:
                    is_prime = False
                    break
            if is_prime:
                if show:
                    print i,
                primes.append(i)
        return primes

# Decide if n is prime given a pre-generated list of primes p that goes up to
#  sqrt(n) but not necessarily n
def is_prime(n,p):
    for i in p:
        if n % i == 0:
            return False
        if i*i > n:
            return True

# Bisection search through sorted list
def inb(n,l):
    low = 0
    up = len(l) - 1
    while up >= low:
        temp = (low + up) / 2
        if n < l[temp]:
            up = temp - 1
        elif n > l[temp]:
            low = temp + 1
        else:
            return temp
    return False

# Generate factors of all of the numbers up to n
def factor(n, show=False):
    p = primes(n)
    factors = [[0],[1]]
    for i in range(2,n+1):
        if inb(i,p):
            factors.append([1,i])
            continue
        for prime in p:
            if i % prime == 0:
                temp = factors[i/prime] + [prime * j for j in factors[i/prime]]
                factors.append(list(set(temp)))
                break
    return factors

# Give the prime factorization of n
def pf(n, show=False):
    p = primes(n+1)
    factors = []
    while n != 1:
        for prime in p:
            if n % prime == 0:
                factors.append(prime)
                n /= prime
    if show:
        d = {}
        for factor in factors:
            if d.get(factor) == None:
                d[factor] = 1
            else:
                d[factor] += 1
        s = ''
        for key in sorted(d.keys()):
            if d[key] == 1:
                s += '(%d)' % key
            else:
                s += '(%d^%d)' % (key,d[key])
        if len(d.keys()) == 1:
            s = s[1:-1]
        print s
    else:
        return factors

# Euclid's GCD algorithm
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)
