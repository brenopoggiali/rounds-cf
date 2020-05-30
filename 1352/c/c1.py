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
	count = 0
	al = []
	i = 1
	while True:
		if i%a != 0:
			count += 1
			al.append(i)
		i += 1
		if count == b:
			break
	print(al[-1], a, b)
	print_array(al)
