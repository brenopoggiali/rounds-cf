n, m = map(int, input().split())

g = [[]]*(n+1)


for i in range(m):
	a, b = map(int, input().split())
	g[a] = g[a][:] + [b]
	g[b] = g[b][:] + [a]


if n==7:
	M = 0
	for i in range(1, n+1):
		for j in range(1, n+1):
			if i == j:
				continue
			N = []
			for k in g[i]+g[j]:
				N.append(k)
			N = set(N)
			num_edges = m - len(g[i]) - len(g[j]) + len(N)
			M = max(M, num_edges)
	print(min(M, 21))
else:
	print(m)
