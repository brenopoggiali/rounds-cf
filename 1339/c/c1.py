from sys import exit

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

def power_of_two():
	pt = []
	for i in range(30):
		pt.append(2**i)
	return pt

t = ii()
pt = power_of_two()
for _ in range(t):
	n = ii()
	a = liis()
	maxi = 0
	soma = 0
	for i in range(1, n):
		a[i] += soma
		if a[i] >= a[i-1]:
				continue
		for j in range(maxi, len(pt)):
			if a[i]+pt[j] >= a[i-1]:
				a[i] = a[i]+pt[j]
				soma += pt[j]
				maxi = max(maxi, j+1)
				break
	print(maxi)

