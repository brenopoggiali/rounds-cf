from sys import stdin, exit
from math import ceil
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	a, b, c, d = iis()
	if b >= a:
		print(b)
	elif (c-d) > 0:
		print(b+ceil((a-b)/(c-d))*c)
	else:
		print(-1)
