t = int(input())

for _ in range(t):
	n = int(input())
	p = list(map(int, input().split()))
	p = sorted(p)[::-1]
	count = 0
	for i in p:
		if i > count:
			count += 1
	print(count)
