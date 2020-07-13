from sys import stdin, exit
from math import gcd
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

def prime_factors(n):
	i = 2
	factors = []
	while i*i <= n:
		if n%i: i += 1
		else:
			n //= i
			factors.append(i)
	if n > 1:
		factors.append(n)
	return factors


t = ii()
for _ in range(t):
	n = ii()	
	primes = prime_factors(n)
	mini = (1, n-1)
	low_lcm = (n-1)//gcd(1, n-1)
	#print(n-1, low_lcm)
	for i in primes:
		new_lcm = (i*(n-i))//gcd(i, n-i)
		#print(n-i, i, new_lcm, i*(n-i), gcd(i, n-i))
		if new_lcm < low_lcm:
			low_lcm = new_lcm
			mini = (i, n-i)
	print(mini[0], mini[1])
	#print('cabou')
