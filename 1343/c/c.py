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
	a = liis()
	soma = 0
	positive = True
	maxi = 0
	for i in a:
		if positive:
			if i > 0:
				maxi = max(maxi, i)
			else:
				soma += maxi
				positive = False
				maxi = i
		else:
			if i < 0:
				maxi = max(maxi, i)
			else:
				soma += maxi
				positive = True
				maxi = i
	soma += maxi
	print(soma)
