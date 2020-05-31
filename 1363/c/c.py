from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))


t = ii()
for _ in range(t):
	n, x = iis()	
	tree = [[] for i in range(n+1)]
	nodes = {}
	for i in range(n-1):
		u, v = iis()
		if u not in nodes:
			nodes[u] = 0
		if v not in nodes:
			nodes[v] = 0
		nodes[u] += 1
		nodes[v] += 1

		tree[u].append(v)
		tree[v].append(u)

	if x not in nodes or nodes[x] == 1:
		print('Ayush')
	else:
		if (n-2)%2 == 0:
			print('Ayush')	
		else:
			print('Ashish')
