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
	if n < 4: print(-1)
	else:
		a = []
		for i in range(2, n+1):
			if i%2 != 0: continue
			a.append(i)
		for i in range(n, -1, -1):
			if i%2 != 1: continue
			a.append(i)
		for i in range(n):
			if abs(a[i]-a[i+1]) < 2:
				if a[i] > a[i+1]:
					a[i-1], a[i], a[i+1], a[i+2] = a[i+1], a[i+2], a[i], a[i-1]
				else:
					a[i-1], a[i], a[i+1], a[i+2] = a[i+2], a[i+1], a[i-1], a[i]
				break
		print_array(a)
