from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	v, c, n, m = iis()	
	can = True
	if v+c < n+m:
		can = False
	 
	
	if can:
		print('Yes')
	else:
		print('No')

