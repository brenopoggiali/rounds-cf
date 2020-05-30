from sys import exit

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print("".join(map(str, a)))

t = ii()
for _ in range(t):
	m, n = iis()	
	ans = [['B' for j in range(n)] for i in range(m)]
	ans[0][0] = 'W'
	for i in range(len(ans)):
		print_array(ans[i])
	 
