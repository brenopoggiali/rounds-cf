from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	n = ii()	
	s = liis()
	s = sorted(s)
	maxi = float("inf")
	for i in range(1, len(s)):
		maxi = min(maxi, s[i]-s[i-1])
	print(maxi)
