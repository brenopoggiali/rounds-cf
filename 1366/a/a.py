from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	a, b = iis()
	count = 0
	first = min(a//2, b)
	second = min(a, b//2)
	maxi = min((a+b)//3, a, b)
	print(max(first, second, maxi))
