n = int(input())
a = list(map(int, input().split()))

sor = sorted(a)

i = 0
while i < n-1:
	if a[i] > sor[i]:
		soma = a[i]+a[i+1]
		size = 2
		ini = i
		cur = i
		used = {a[i+1]: 1}
		if a[i+1] == a[i]: cur += 1
		while (i+2 < n and soma/size > sor[cur]):
			i += 1
			soma += a[i+1]
			size += 1
			if a[i+1] in used:
				used[a[i+1]] += 1
			else:
				used[a[i+1]] = 1
			while sor[cur] in used:
				if sor[cur] == 0: break
				sor[cur] -= 1
				cur += 1
		for j in range(ini, i+2):
			a[j] = soma/size
	else:
		a[i] = a[i]
	i += 1

for i in a:
	print('%.9f' % i)
	
