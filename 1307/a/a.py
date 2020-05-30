from sys import exit

def iis(): return map(int, input().split())
def ii(): return int(input())
def liis():	return list(map(int, input().split()))

t = ii()
for _ in range(t):
	n, d = iis()
	a = liis()
	ans = a[0]
	for i in range(1, len(a)):
		for j in range(a[i]):
			d -= i
			if d < 0: break
			ans += 1
		if d < 0: break
	print(ans)
