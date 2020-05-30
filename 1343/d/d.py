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
	a = liis()
	counter = {}
	poss = []
	add = [0 for i in range(2*k+2)]
	rem = [0 for i in range(2*k+2)]
	alt = [0 for i in range(2*k+2)]
	
	for i in range(n//2):
		ini = a[i]	
		fim = a[n-i-1]
		mini = 1+min(ini, fim)
		maxi = k+max(ini, fim)
		alt[ini+fim] += 1
		add[mini] += 1
		rem[maxi+1] += 1
	
	count = 0
	for i in range(2, len(add)-1):
		count += add[i]-rem[i]
		two = ((n//2)-count)*2
		poss.append(count-alt[i]+two)
	
	print(min(poss))
				


