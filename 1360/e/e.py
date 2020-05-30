from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))


def is_valid(pol, i, j, valids):
	valid1 = True
	for k in range(j, len(pol)):
		if valids[i][k]: break
		if pol[i][k] != 1:
			valid1 = False
			break
	valid2 = True
	for k in range(i, len(pol)):
		if valids[k][j]: break
		if pol[k][j] != 1:
			valid2 = False
			break
	return valid1 or valid2


t = ii()
for _ in range(t):
	n = ii()	
	pol = []
	for i in range(n):
		a = input()
		pol.append([])
		for j in str(a):
			try:
				pol[i].append(int(j))
			except:
				continue
	valids = [[False for i in range(n)] for i in range(n)] 
	
	can = True
	for i in range(n-1, -1, -1):
		for j in range(n-1, -1, -1):
			if pol[i][j] == 1:
				if not is_valid(pol, i, j, valids):
					can = False
					break
				else:
					valids[i][j] = True
		if not can:
			break

	if can:
		print('YES')
	else:
		print('NO')
