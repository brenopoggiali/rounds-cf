from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	a, b = iis()	
	for i in range(b-1):
		mini = '9'
		maxi = '0'
		for c in str(a):
			if int(c) < int(mini):
				mini = c
			if int(c) > int(maxi):
				maxi = c
		a += (int(maxi)*int(mini))
		if mini == '0':
			break
	print(a)
