from sys import exit

def iis(): return map(int, input().split())
def ii(): return int(input())
def liis():	return list(map(int, input().split()))

t = ii()
for _ in range(t):
	a, b, c = iis()
	a = sorted([a, b, c])[::-1]
	a, b, c = a[0], a[1], a[2]
	count = 0
	if a >= 1:
		count += 1
		a -= 1
	if b >= 1:
		count += 1
		b -= 1
	if c >= 1:
		count += 1
		c -= 1
	if a >= 1 and b >= 1:
		count += 1
		a -= 1
		b -= 1
	if a >= 1 and c >= 1:
		count += 1
		a -= 1
		c -= 1
	if b >= 1 and c >= 1:
		count += 1
		b -= 1
		c -= 1
	if b >= 1 and a >= 1 and c >= 1:
		count += 1
	print(count)
