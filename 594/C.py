n, m = map(int, input().split())
ans = [0,1,2,3,5]

for i in range(5, max(m, n)+1):
	ans.append((ans[i-2] + 2*ans[i-3] + ans[i-4])%(10**9+7))

print((2*(ans[n]+ans[m]-1))%(10**9+7))
