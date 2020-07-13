from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

def check(a, s):
	init = 0
	for i in range(len(a)):
		if a[i] != s[i]:
			init = i
			break
	end = 0
	for i in range(len(a)-1, -1, -1):
		if a[i] != s[i]:
			end = i
			break
	#print(init, end)
	for i in range(init, end+1):
		if a[i] == s[i]:
			print(2)
			break 
	else:
		print(1)


t = ii()
for _ in range(t):
	n = ii()	
	a = liis()
	s = sorted(a)
	if s == a:
		print(0)
	else:
		for i in range(len(a)):
			if a[i] == s[i]:
				check(a, s)
				break
		else:
			print(1)		
