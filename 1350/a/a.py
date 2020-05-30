from sys import stdin, exit
from math import ceil, sqrt
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	n, k = iis()	
	can = False
	orig = n
	if orig%2 == 0:
		print(n + (k)*2)
	else:
		found = False
		for i in range(2, ceil(sqrt(n))+1):
			if n%i == 0:
				n += i
				k -= 1
				found = True
				break
		if not found:
			n += n
			k -= 1
		print(n + (k)*2)
