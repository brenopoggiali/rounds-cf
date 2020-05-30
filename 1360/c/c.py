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
	l = sorted(liis())
	odd, even = 0, 0
	for i in l:
		if i%2 == 0:
			even += 1
		else:
			odd += 1
	for i in range(1, n):
		if odd%2 == 0 and even%2 == 0:
			break
		if l[i-1]+1 == l[i]:
			odd -= 1
			even -= 1
	if odd%2 == 0 and even%2 == 0:
		print("YES")
	else:
		print("NO")
