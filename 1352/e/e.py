from sys import stdin, exit
from collections import Counter
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
	ma = max(a)
	aset = Counter(a) 
	count = 0
	for i in range(len(a)):
		soma = a[i]
		for j in range(i+1, len(a)):
			soma += a[j]
			if soma in aset: 
				count += aset[soma]
				del aset[soma]
			elif soma > ma: break
	print(count)

