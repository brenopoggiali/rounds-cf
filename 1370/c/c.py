from sys import stdin, exit
from math import sqrt
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

ff = 'FastestFinger'
ashi = 'Ashishgup'

def prime_factors(n):
	prime = []
	while n%2 == 0:
		prime.append(2)
		n = n//2
	for i in range(3, int(sqrt(n))+1, 2):
		while n%i == 0:
			prime.append(i)
			n = n//i
	if n > 2:
		prime.append(n)
	return prime


t = ii()
for _ in range(t):
	n = ii()		
	first = False
	second = False
	if n == 1:
		first = True
	elif n%2 == 1:
		second = True
	elif n == 2:
		second = True
	else:
		primes = prime_factors(n)
		count = 0
		twos = 0
		for i in primes:
			if i%2 == 1:
				count += 1
			else:
				twos += 1
		if twos == 1 and count == 1:
			first = True
		elif count >= 1:
			second = True
		#elif count == 1 and len(primes)-1:
			
		else:
			first = True

		#print(primes)

	if first:
		print(ff)
	else:
		print(ashi)
