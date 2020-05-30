from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)), end=" ")

t = ii()
for _ in range(t):
	n = ii()
	div = n//2
	if div%2 == 0:
		print("YES")
		par, impar = [], []
		for i in range(1, n+1):
			if i%2 == 0:
				par.append(i)
			else:
				impar.append(i)
		impar[-1] += len(par)
		print_array(par)
		print_array(impar)
		print()
	else:
		print("NO")
	
