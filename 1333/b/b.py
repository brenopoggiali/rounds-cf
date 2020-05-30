from sys import exit

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	n = ii()
	a = liis()
	b = liis()
	can = True
	options = set()
	
	for i in range(n):
		#print(b[i], a[i], options)
		if b[i] == a[i]:
			options.add(a[i])
			continue
		elif b[i] < a[i]:
			if -1 not in options:
				can = False
				break
		else:
			if 1 not in options:
				can = False
				break
		options.add(a[i])
	
	if can:
		print("YES")
	else:
		print("NO")
