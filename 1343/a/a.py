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
	c = 1
	for i in range(1, n):
		c += 2**i
		if n%c == 0:
			print(n//c)
			break

	
