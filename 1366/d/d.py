from sys import stdin, exit
import itertools
from math import gcd
input = stdin.readline

def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))


def prime_factors(n):
    for i in itertools.chain([2], itertools.count(3, 2)):
        if n <= 1:
            break
        while n % i == 0:
            n //= i
            yield i


t = ii()
a = iis()
d1 = []
d2 = []
for i in a:
    can = False
    primes = list(set(prime_factors(i)))
    for idx, prime1 in enumerate(primes[:-1]):
        if gcd(prime1+primes[idx+1], i) == 1:
            can = True
            d1.append(prime1)
            d2.append(primes[idx+1])
            break
    if not can:
        d1.append(-1)
        d2.append(-1)


print_array(d1)
print_array(d2)
