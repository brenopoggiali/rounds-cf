from random import shuffle
n = int(input())
a = list(map(int, input().split()))

def f(x, y):
	return (x|y)-y
	
def func(a):
	atual = a[0]
	for i in range(1, len(a)):
		atual = f(atual, a[i])
	return atual	

a = sorted(a)[::-1]
for i in range(n):
	for j in range(32):
		if (v[i])&(1<<j):
			if bits[j]

print(" ".join(map(str, (a))))
