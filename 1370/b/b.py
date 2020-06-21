from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	n = ii()	
	l = liis()
	odds = []
	evens = []
	for idx, i in enumerate(l):
		if i%2 == 0:
			evens.append([i, idx+1])
		else:
			odds.append([i, idx+1])
	if len(evens)%2==0:
		if len(evens) > 0:
			evens.pop()
			evens.pop()
		else:
			odds.pop()
			odds.pop()
	else:
		evens.pop()
		odds.pop()
	#print(evens, odds)
	for i in range(len(evens)//2):
		print(evens[i][1], evens[len(evens)-1-i][1])
	for i in range(len(odds)//2):
		print(odds[i][1], odds[len(odds)-1-i][1])
