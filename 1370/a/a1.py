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
	maxi = 0
	print(n//2)
	'''
	for i in range(1, n+1):
		for j in range(i+1, n+1):
			#print(gcd(i, j))
			maxi = max(maxi, gcd(i, j))
	print(maxi)
	'''
