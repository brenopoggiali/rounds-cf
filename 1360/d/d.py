import collections
import itertools
from sys import stdin, exit
from math import ceil, sqrt
input = stdin.readline


def iis(): return map(int, input().split())


def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n /= i
            yield i
        else:
            i += 1

    if n > 1:
        yield n


def prod(iterable):
    result = 1
    for i in iterable:
        result *= i
    return result


def get_divisors(n):
    pf = prime_factors(n)

    pf_with_multiplicity = collections.Counter(pf)

    powers = [
        [factor ** i for i in range(count + 1)]
        for factor, count in pf_with_multiplicity.items()
    ]

    for prime_power_combo in itertools.product(*powers):
        yield int(prod(prime_power_combo))


t = int(input())
for _ in range(t):
    n, k = iis()
    divs = sorted(list(get_divisors(n)))[::-1]
    for i in divs:
        if i <= k:
            print(n//i)
            break
