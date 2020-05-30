from sys import exit

def iis(): return map(int, input().split())
def ii(): return int(input())
def liis():	return list(map(int, input().split()))

def getsize(a, b, x, y):
	ans = 0
	ans = max(ans, (x)*b)
	ans = max(ans, (a-x-1)*b)
	ans = max(ans, a*(y))
	ans = max(ans, a*(b-y-1))
	return ans 

t = ii()
for _ in range(t):
	a, b, x, y = iis()
	ans = getsize(a, b, x, y)
	print(ans)
