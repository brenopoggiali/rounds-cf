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
	a = sorted(liis())
	ans = 1
	for i in range(n-1, -1, -1):
		if a[i] <= i+1:
			ans += i+1
			break

	print(ans)
