from sys import exit

def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))

t = ii()
for _ in range(t):
	n, x, y = iis()
	if x > y: x, y = y, x		

	if x + y < n:
		mini = 1
	else:
		mini = min(n, (x+y+1)-n)

	if x + y > n:
		maxi = n
	else:
		maxi = x+y-1
	
	print(mini, maxi)
