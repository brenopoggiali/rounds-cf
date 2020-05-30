from math import ceil

t = int(input())
for i in range(t):
	a,b,c,d,k = map(int, input().split())
	x = ceil(a/c)
	y = ceil(b/d)
	if x+y > k:
		print("-1")
	else:
		print(x, y)
