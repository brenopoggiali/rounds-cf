from sys import exit
from bisect import bisect

def iis(): return map(int, input().split())
def ii(): return int(input())
def liis():	return list(map(int, input().split()))

t = ii()
for _ in range(t):
	n = ii()
	b = liis()
	todos = []
	duplas = []
	for i in range(1, 2*n+1):
		if i not in b:
			todos.append(i)
	flag = False
	for i in b:
		a = bisect(todos, i)
		if a >= len(todos): 
			flag = True
			break
		duplas.append([i, todos[a]])
		todos[a] = -1
		todos = sorted(todos)
	if flag:
		print(-1)
	else:
		for dupla in duplas:
			print(" ".join(map(str, dupla)), end=" ")
		print()
