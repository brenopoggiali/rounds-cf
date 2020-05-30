from math import gcd

q = int(input())

for _ in range(q):
	a, b, n, S = map(int, input().split())
	if a*n + b*1 < S:
		print("NO")
	elif a*n + b*1 == S:
		print("YES")
	else:
		aux = S//n
		S -= min(n*aux, a*n)
		if b >= S:
			print("YES")
		else:
			print("NO")
		

