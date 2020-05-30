from sys import exit
from math import gcd

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	n = ii()
	a = liis()
	ans = [0 for _ in range(n)]
	primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
	color = 0
	for prime in primes:
		first = True
		for idx, i in enumerate(a):
			if ans[idx] == 0 and i%prime == 0:
				if first: color+=1
				ans[idx] = color
				first = False

	print(color)
	print_array(ans)
	
