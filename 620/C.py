q = int(input())

for _ in range(q):
	n, m = map(int, input().split())
	mini = m
	maxi = m
	ctime = 0
	can = True
	#print("m\tt\tmini\tmaxi\tl\th")
	for __ in range(n):
		t, l, h = map(int, input().split())		
		mini = max(mini-(t-ctime), l)
		maxi = min(maxi+(t-ctime), h)
		#print(m,'\t', t,'\t', mini, '\t', maxi, '\t', l, '\t', h)
		if (maxi >= l and mini <= h):
			ctime = t
			continue
		else:
			can = False
	if can:
		print("YES")
	else:
		print("NO")
