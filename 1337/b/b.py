from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	x, n, m = iis()
	for i in range(n):
		nexti = (x//2)+10
		if nexti < x:
			x = nexti

	for i in range(m):
		x -= 10
	if x <= 0:
		print("YES")
	else:
		print("NO")
