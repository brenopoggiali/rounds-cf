from sys import exit

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	n, x = iis()
	a = liis()
	a = set(a)

	numbers = [i for i in range(1, 300)]
	for i in numbers:
		if x == 0 and i not in a:
			break
		current = i
		if i not in a:
			x -= 1
	print(current)
