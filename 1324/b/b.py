from sys import exit
from collections import Counter

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))


t = ii()
for _ in range(t):
	n = ii()
	a = liis()
	contador = {}
	for idx, i in enumerate(a):
		if i not in contador:
			contador[i] = []
		contador[i].append(idx)
	evens = 0
	odds = 0
	can = False
	
	for k, v in contador.items():
		if len(v) > 2:
			can = True
		elif len(v) == 2:
			if abs(v[0]-v[1]) > 1:
				can = True 
		if can:
			break
	
	if can:
		print("YES")
	else:
		print("NO")
