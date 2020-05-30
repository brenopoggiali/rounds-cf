from sys import exit

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	n = ii()
	kings = set()
	prins = set()
	for i in range(1, n+1):
		kings.add(i)
		prins.add(i)
	for i in range(1, n+1):
		l = liis()
		for j in range(1, len(l)):
			if l[j] in kings:
				kings.remove(l[j])
				prins.remove(i)
				print(kings, prins)
				break
	print(kings, prins)
	if len(kings) and len(prins):
		print("IMPROVE")
		for i in kings:
			print(i, end=" ")
			break
		for i in prins:
			print(i)
			break	
	else:
		print("OPTIMAL")
