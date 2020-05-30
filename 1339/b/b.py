from sys import exit
from collections import deque

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	n = ii()
	a = deque(sorted(liis()))
	ans = []
	bol = True
	for i in range(n):
		if bol:
			ans.append(a.popleft())
		else:
			ans.append(a.pop())
		bol = not bol
	ans = ans[::-1]
	print_array(ans)


