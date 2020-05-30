from math import sqrt, log

primes = [2]

def g(x, n):
	ans = int(log(x, n))
	return n**ans

def is_prime(n):
	if n == 2:
		return True
	else:
		if n%2 == 0:
			return False
		for i in range(3, round(sqrt(n))+1, 2):
			if n%i == 0:
				return False
		return True

def f(x, n):
	for i in range(primes[len(primes)-1]+1, x):
		if is_prime(i):
			primes.append(i)
	answer = 1
	for i in range(len(primes)):
		if x%primes[i] == 0:
			if primes[i] == 5: print(n, primes[i], g(n, primes[i]))
			answer *= g(n, primes[i])
	return answer	


x, n = map(int, input().split())
answer = 1
for i in range(1, n+1):
	answer *= f(x, i)


print(answer%1000000007)
