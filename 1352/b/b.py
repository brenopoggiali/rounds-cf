from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	n, k = iis()
	if (n-(2*(k-1)))%2 == 0 and (n-(2*(k-1))) > 0:
		print("YES")
		a = []
		for i in range(k-1):
			a.append(2)	
		a.append(n-sum(a))
		print_array(a)
	elif (n-(1*(k-1)))%2 == 1 and (n-(1*(k-1))) > 0:
		print("YES")
		a = []
		for i in range(k-1):
			a.append(1)	
		a.append(n-sum(a))
		print_array(a)
	else:
		print("NO")
