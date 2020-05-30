from sys import stdin, exit
from collections import deque
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

inp = []
n, k = iis()

inp.append(n)
inp.append(k)
for i in range(n-1):
	l = liis()
	for i in l:
		inp.append(i)
#print(inp)
ii = 0
n = inp[ii]; ii += 1
k = inp[ii]; ii += 1

coupl = [[] for _ in range(n)]
for _ in range(n-1):
	u = inp[ii]-1; ii += 1
	v = inp[ii]-1; ii += 1
	coupl[u].append(v)
	coupl[v].append(u)

root = 0
bfs = [root]
P = [-1]*n
for node in bfs:
	for nei in coupl[node]:
		del coupl[nei][coupl[nei].index(node)]
		bfs.append(nei)
		P[nei] = node

size = [1]*n
for node in reversed(bfs[1:]):
	size[P[node]] += size[node]

depth = [0]*n
for node in bfs[1:]:
	depth[node] = depth[P[node]]+1

ans = [depth[node]-size[node]+1 for node in range(n)]

print(sum(sorted(ans, reverse=True)[:k]))

