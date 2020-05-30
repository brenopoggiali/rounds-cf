from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):	
	n, k = iis()
	a = liis()
	b = liis()
	a = sorted(a)
	b = sorted(b)[::-1]
	i = 0
	while i < n and a[i] < b[i] and k > 0:
		a[i], b[i] = b[i], a[i]
		i += 1
		k -= 1
	#print(a, b, a[i], b[-1-i])
	print(sum(a))
