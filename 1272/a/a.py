from sys import exit

def iis(): return map(int, input().split())
def ii(): return int(input())
def liis():	return list(map(int, input().split()))

def tp(a, b, c):
	return abs(a-b) + abs(a-c) + abs(b-c)

t = ii()
for _ in range(t):
	a, b, c = iis()
	ans = tp(a+1, b+1, c+1)
	for i in range(3):
		for j in range(3):
			for k in range(3):
				ans = min(ans, tp(a-i-1, b-j-1, c-k-1))
	print(ans)
	
exit(0)
