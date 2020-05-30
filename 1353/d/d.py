from sys import stdin, exit
from heapq import heappush, heappop
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

def binary(a, l, r, i):
	if (r-l+1)%2 == 1:
		return (l+r)//2
	return (l+r-1)//2

def solve(a, l, r, i):
	ans = a
	tupla = (-len(a), 0, len(a)-1, ans)
	a = []
	heappush(a, tupla)
	#print(a)
	while len(a):
		size, ini, fim, cur = heappop(a)
		split = binary(cur, ini, fim, i)
		if ans[split] != 0: continue
		ans[split] = i
		#teste = input()
		left = ans[ini:split]
		right = ans[split+1:fim+1]
		#print(i, "cur, split, left, right: ", cur, split, left, right)
		if len(right) > len(left):
			if len(right) > 0:
				heappush(a, (-len(right), split+1, fim, right))
			if len(left) > 0:
				heappush(a, (-len(left), ini, split-1, left))
		else:
			if len(left) > 0:
				heappush(a, (-len(left), ini, split-1, left))
			if len(right) > 0:
				heappush(a, (-len(right), split+1, fim, right))
		#print(a)
		#a = deque(sorted(a))
		i += 1
	return ans
	


t = ii()
for _ in range(t):
	n = ii()
	a = [0]*n	
	a = solve(a, 0, n-1, 1)
	#print("ANSWER")
	print_array(a)
