t = int(input())

for _ in range(t):
	n = int(input())
	flag = False
	a = list(map(int, input().split()))
	soma = sum(a)
	if soma%2 == 1:
		print("YES")
		continue
	for i in range(n):
		for j in range(i+1, n):
			if (soma-a[i]+a[j])%2 == 1 or (soma-a[j]+a[i]%2) == 1:
				print("YES")
				flag = True
				break
		if flag:
			break
	if not flag:
		print("NO")
