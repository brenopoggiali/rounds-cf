from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	x, y = iis()	
	a, b = iis()
	op = []
	op.append((abs(x)+abs(y))*a)
	if b < a*2:
		op.append(abs(x)*b+abs((y-x)*a))
		op.append(abs(y)*b+abs((x-y)*a))
		op.append(abs(x-y)*a+abs(min(abs(x), abs(y))*b))
		op.append(abs(y-x)*a+abs(min(abs(x), abs(y))*b))
	print(min(op))	
