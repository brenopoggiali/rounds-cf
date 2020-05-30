t = int(input())

for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	count = 0
	for i in range(len(a)):
		if a[i] == 0:
			count += 1
			a[i] += 1
	if sum(a) == 0:
		print(count + 1)
	else:
		print(count)
