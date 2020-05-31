from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	s = input().strip()
	qnt = []
	ones, zeros = 0, 0
	for i in s:
		qnt.append([zeros, ones, 0, 0, i])
		if i == '1':
			ones += 1
		else:
			zeros += 1

	
	zeros, ones = 0, 0

	idx = len(qnt)-1
	for i in s[::-1]:
		qnt[idx][2] = zeros	
		qnt[idx][3] = ones
		if i == '1':
			ones += 1
		else:
			zeros += 1
		idx -= 1

	#print(qnt)
	mini = float("inf")
	for i in qnt:
		mini = min(mini, i[0]+i[3], i[1]+i[2])
		if i[4] == '1':
			mini = min(mini, i[0]+i[2])
		else:
			mini = min(mini, i[1]+i[3])
		#print(mini)
	
	print(mini)
