from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	n, x = iis()	
	a = liis()
	soma = sum(a)
	if soma%x != 0:
		print(n)
	else:
		for i in range(n):
			if a[i]%x != 0:
				break
		for j in range(n):
			if a[-j-1]%x != 0:
				break
		#print('aqui', i, j)
		if (i!=n or j != n) and n-min(i, j)-1 != 0:
			print(n-min(i, j)-1)
		else:
			print(-1)
