from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print("".join(map(str, a)))


alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
t = ii()
for _ in range(t):
	n, a, b = iis()
	s = alphabet[:b]	
	ans = []
	for i in range(n):
		ans.append(s[i%len(s)])
	print_array(ans)
