from sys import stdin, exit
from collections import deque
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	n  = ii()	
	A = deque(liis())
	a, b = 0, 0
	moves = 1
	ap, bp = 0, n-2
	is_alice = False
	quantity = 0
	a += A.popleft()
	last_move = a
	while len(A):
		if is_alice:
			conta = 0
			doces = 0
			for i in range(len(A)):
				conta += A.popleft()	
				doces += 1
				if conta > last_move:
					break
			a += conta
		else:
			conta = 0
			doces = 0
			for i in range(bp, -1, -1):
				conta += A.pop()
				doces += 1
				if conta > last_move:
					break
			b += conta
		moves += 1
		last_move = conta
		bp -= doces
		is_alice = not is_alice
	print(moves, a, b)
