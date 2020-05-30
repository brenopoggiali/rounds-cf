from sys import exit

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	n = ii()
	h = iis()
	evens, odds = 0, 0
	for i in h:
		if i%2 == 0:
			evens+=1
		else:
			odds += 1
	if evens == 0 or odds == 0:
		print("YES")
	else:
		print("NO")
