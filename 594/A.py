t = int(input())
for _ in range(t):
	n = int(input())
	pi = list(map(int, input().split()))
	m = int(input())
	qi = list(map(int, input().split()))
	count = 0
	pares1, pares2 = 0, 0
	impares1, impares2 = 0, 0
	for ind1, i in enumerate(pi):
		if i%2 == 0:
			pares1 += 1
		else:
			impares1 += 1

	for ind2, j in enumerate(qi):
		if j%2 == 0:
			pares2 += 1
		else:
			impares2 += 1
	count = pares1*pares2 + impares1*impares2
	print(count)
