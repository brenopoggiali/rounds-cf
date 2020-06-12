from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	n, m = iis()
	matrix = []
	for i in range(n):
		a = liis()
		matrix.append(a)
	if n > m:
		new_matrix = []
		for i in range(m):
			new_matrix.append([])
			for j in range(n):
				new_matrix[i].append(matrix[j][i])
		matrix = new_matrix
		n, m = m, n
	#for i in range(n):
	#	print(matrix[i])


	count = 0
#	print('i, zerosF, zerosS, onesF, onesS')
	for i in range(m):
		zerosF = onesF = zerosS = onesS = 0
		jose = False
		passaram = set()
		if i > m-i-1+n-1:
			#print('breko', i)
			break

		for j in range(min(i+1, n)):
			passaram.add((j, i-j))
			if matrix[j][i-j] == 0:
				zerosF += 1
			else:
				onesF += 1
		for j in range(min(i+1, n)):
			#print(n-j-1, m-i+j-1)
			if (n-j-1, m-i+j-1) in passaram:
				jose = True
			if matrix[n-j-1][m-i+j-1]	== 0:
				zerosS += 1
			else:
				onesS += 1
		if jose: break 
		count += min(zerosS+zerosF, onesS+onesF)
#		print(i, zerosF, zerosS, onesF, onesS, count)

	print(count)	
