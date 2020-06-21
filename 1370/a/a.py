from sys import stdin, exit
from math import gcd
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	n = ii()	
	if n < 4:
		print(1)
	else:
		if n%2 == 0:
			print(gcd(n,(n-2)))
		else:
			print(gcd((n-1), (n-3)))
			
