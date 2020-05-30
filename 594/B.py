from math import ceil

n = int(input())
a = list(map(int, input().split()))
a = sorted(a)

x, y = 0, 0
for i in range(ceil(n/2)):
	j = n-i-1
	x += a[j]
	if i != j:
		y += a[i]
print(x**2+y**2)
