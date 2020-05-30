from sys import exit

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	a, b = iis()
	div = a//b
	if b*div == a:
		print(0) 
	else:
		print(b*(div+1)-a)
