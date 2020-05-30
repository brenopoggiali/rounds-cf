n, m, k = map(int, input().split())

a = []
for _ in range(n):
	a.append(list(map(int, input().split())))

count = 0

for i in range(len(a)-1):
	ini, fim = 0, k-1
	big_k = sum(a[i][:k]) + sum(a[i+1][:k])
	cur = big_k
	for j in range(k, len(a[i])):
		big_k = big_k - a[i][j-k] - a[i+1][j-k]
		big_k += a[i][j] + a[i+1][j]
		if big_k > cur:
			cur = big_k
			ini = j-k+1
			fim = j
		elif big_k == cur:
			linha = a[i][j-k+1:j+1]
			cur_linha = a[i][ini:fim+1]
			if sum(linha) > sum(cur_linha):
				cur = big_k
				ini = j-k+1
				fim = j
	
	count += cur
	for j in range(ini, fim+1):
		a[i][j] = 0
		a[i+1][j] = 0

last = sum(a[-1][:k])
ini = 0
fim = k-1
cur = last
for j in range(k, len(a[0])):
	last -= a[-1][j-k]
	last += a[-1][j]
	if last > cur:
		cur = last
		ini = j-k+1
		fim = j
for j in range(ini, fim+1):
	a[-1][j] = 0
count += cur
print(count)
