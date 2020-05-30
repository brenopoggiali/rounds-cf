from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print("".join(map(str, a)))

t = ii()
for _ in range(t):
	n1, n2, n3 = iis()	
	ans = []
	if n2 == 0 and n3 == 0:
		print('0'*(n1+1))
		continue
	if n1 == 0 and n2 == 0:
		print('1'*(n3+1))
		continue
	if n1 == 0 and n3 == 0:
		for i in range(n2+1):
			if i%2 == 0: ans.append(0)
			else: ans.append(1)
		print_array(ans)
		continue
	for i in range(n1+1): ans.append(0)
	for i in range(n3+1): ans.append(1)
	for i in range(n2-1): 
			if i%2 == 0: ans.append(0) 
			else: ans.append(1)
	print_array(ans)
