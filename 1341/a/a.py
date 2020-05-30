from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	n, a, b, c, d = iis()	
	can = False
	if (a+b)*n >= c-d and (a-b)*n <= c+d:
		can = True
	'''
	for i in range(c-d, c+d+1):
		if i%n == 0 and i//n >= a-b and i//n <= a+b:
			can = True
			print(i, i//n)
			break
	'''
	if can:
		print("Yes")
	else:
		print("No")
