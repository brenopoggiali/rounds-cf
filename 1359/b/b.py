from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
		n, m, x, y = iis()
		sq = []
		for i in range(n):
			a = input().strip()
			sq.append([])
			for c in a:
				sq[i].append(c)
		count = 0
		if y > 2*x:
			y = 2*x
		for i in range(len(sq)):
			for j in range(len(sq[i])):
				if sq[i][j] == '.':
					if j < len(sq[i])-1:
						if sq[i][j+1] == '.':
							count += y
							sq[i][j+1] = '*'
						else:
							count += x
					else:
						count += x
		print(count)
