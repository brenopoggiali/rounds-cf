from math import ceil, gcd

n, p, w, d = map(int, input().split())

if p > n*w or p%gcd(w,d)!=0 or (p < d and p != 0):
	print(-1)
else:
	wins, draws = 0, 0
	pts = ceil(p/w)*w
	wins = ceil(p/w)
	dif = d-w
	while(pts != p):
		draws+=1
		wins-=1
		pts += dif
	print(wins, draws, (n-wins-draws))
