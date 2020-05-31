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
	s = []
	for i in range(k):
		a = set(liis()[1:])
		s.append(a)
	password = [-1 for i in range(k)]
	for i, c in enumerate(password):
		for j in range(n, -1, -1):
			if j not in s[i]:
				password[i] = j
				break
	
	print("!", end=" ")
	for c in password:
		print(c, end=" ")
	print()
	input()
