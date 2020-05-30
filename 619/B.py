t = int(input())

for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	ns = []
	for i in range(len(a)):
		if a[i] == -1:
			if i > 0 and a[i-1] != -1:
				ns.append(a[i-1])
			if i < n-1 and a[i+1] != -1:
				ns.append(a[i+1])
	if len(ns) == 0:
		mini = 1
		maxi = 1
	else:
		mini = min(ns)
		maxi = max(ns)
	k = (mini+maxi)//2
	m = 0
	for i in range(1, len(a)):
		if a[i-1] == -1:
			a[i-1] = k
		if a[i] == -1:
			a[i] = k
		m = max(m, abs(a[i]-a[i-1]))
	print(m, k)


