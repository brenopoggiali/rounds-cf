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
	n, k = iis()	
	if k < n:
		print(k)
	else:
		cada = ceil(k/(n-1))
		resto = cada*n
		final = resto - ((n-1)*cada-k)-1
		print(final)
		#print(resto, (n-1)*cada)
