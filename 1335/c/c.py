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
	count = Counter(a)
	maxi = 0
	seti = set(a)
	for key, value in count.items():
		maxi = max(maxi, value)
	print(min(maxi, max(len(seti)-1, min(len(seti), maxi-1))))

