from sys import exit

def iis(): return map(int, input().split())
def ii(): return int(input())
def liis():	return list(map(int, input().split()))

t = ii()
for _ in range(t):
	n, x = iis()
	a = liis()
	maxi = max(a)
	if x in a:
		print(1)
	elif x%maxi == 0:
		print(x//maxi)
	else:
		if x//maxi == 0:
			print(2)
		else:
			print(x//maxi+1)
