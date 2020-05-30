from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	i = input().strip()
	ans = []
	missing = len(i)-1
	for c in range(len(i)):
		if i[c] != '0':
			a = '0'*missing
			b = str(i[c])
			aa = b+a
			ans.append(aa)
		missing -=1
	print(len(ans))
	print_array(ans)
