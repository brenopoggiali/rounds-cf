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
	count = 0
	while n != 1 and n%3 == 0:
		if n%6 == 0:
			n //= 6
		else:
			n *= 2
		count += 1

	if n == 1:
		print(count)
	else:
		print(-1)
