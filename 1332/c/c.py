from sys import exit
from collections import Counter

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	n, k = iis()
	s = input()
	print(Counter(s))
	diffs = set()
	count = 0
	for i in range(n-k):
		if s[i] != s[i+k]:
			diffs.add((i, i+k))
	
	for i in range(n//2):
		if s[i] != s[n-1-i]:
			diffs.add((i, n-1-i))


	diffs = list(diffs)
	for i in range(len(diffs)):
		for j in range(i+1, len(diffs)):
			if diffs[i][0] == diffs[j][0] or diffs[i][0] == diffs[j][1] or diffs[i][1] == diffs[j][0] or diffs[i][1] == diffs[j][1]:
				count += 1	

	#print(count)
	#print(len(diffs)-count)
	#print(sorted(list(diffs)))
