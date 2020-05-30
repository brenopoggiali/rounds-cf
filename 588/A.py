c = list(map(int, input().split()))
c = sorted(c)

if c[0]+c[1]+c[2] == c[3] or c[0]+c[2] == c[1]+c[3] or c[3]+c[0] == c[1]+c[2] or c[3]+c[1] == c[0]+c[2]:
	print("YES")
else:
	print("NO")

