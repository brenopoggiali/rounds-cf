from sys import exit

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	l, r, d, u = iis()
	x, y, x1, y1, x2, y2 = iis()
	y1, y2 = min(y1, y2), max(y1, y2)
	x1, x2 = min(x1, x2), max(x1, x2)
	can = True
	if y-d+u > y2: can = False
	if y+u-d < y1: can = False
	if x-l+r > x2: can = False
	if x+r-l < x1: can = False
	if x1 == x2 and (l != 0 or r != 0): can = False
	if y1 == y2 and (u != 0 or d != 0): can = False
	
	if can:
		print("Yes")
	else:
		print("No")
