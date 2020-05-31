from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	n, x = iis()	
	a = liis()
	odds, evens = 0, 0
	for i in a:
		if i%2 == 0:
			evens += 1
		else:
			odds += 1
	x -= min(evens, x-1)
	if (x == 1 and odds > 0) or (x%2 == 1 and odds >= x) or (x%2 == 0 and odds > x and evens > 0):
		print("Yes")
	else:
		print("No")
