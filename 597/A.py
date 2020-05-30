from math import gcd

n = int(input())

for _ in range(n):
	a, b = map(int, input().split())
	if gcd(a,b) == 1:
		print("Finite")
	else:
		print("Infinite")
