t = int(input())

for _ in range(t):
	n, m = map(int, input().split())
	k = (n-m)//(m+1)
	r = (n-m)%(m+1)
	sem = r*((k+1)*(k+2)//2) + (m+1-r)*((k*(k+1))//2)
	todos = (n*(n+1))//2
	ans = todos-sem
	print(ans)

