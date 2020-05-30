q = int(input())

for _ in range(q):
	n = int(input())
	p = list(map(int, input().split()))
	poss = set()
	for i in range(0, n-1):
		poss.add(i)
	count = 0
	
	while len(poss) > 0 and count < n and p != sorted(p):
		m = sorted(p)[count]
		for i in range(len(p)):
			if p[i] == m:
				ind = i
				break
		if ind-1 in poss and p[ind-1] > p[ind]:
			poss.remove(ind-1)
			p = p[:ind-1] + [p[ind]] + [p[ind-1]] + p[ind+1:]
		else:	
			count += 1
	for i in range(len(p)):
		p[i] = str(p[i])


	print(" ".join(p))
