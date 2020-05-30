t = int(input())

for _ in range(t):
	x, y, a, b = map(int, input().split())
	t = (y-x)//(a+b)
	if ((y-x)/(a+b))%1 == 0:
		print(t)
	else:
		print(-1)
