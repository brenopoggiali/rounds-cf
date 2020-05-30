from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	n = ii()
	a = liis()
	alph = []	
	for i in range(26):
		alph.append([0 for i in range(n)])
	for idx, i in enumerate(a):
		if idx == 0:
			for c in range(len(alph)):
				if c+1 == i:
					alph[c][idx] = 1
		else:
			for c in range(len(alph)):
				alph[c][idx] = alph[c][idx-1]
				if c+1 == i:
					alph[c][idx] += 1
	maxi = 0
	for i in range(26):
		if alph[i][-1] == 0: continue
		for j in range(26):
			if i == j:
				maxi = max(maxi, alph[i][-1])
			elif alph[j][-1] == 0:
				continue
			else:
				for k in range(n):
					x = alph[i][k]
					for l in range(k+1, n-1):
						x2 = alph[i][-1]-alph[i][l]
						y = alph[j][l]-alph[j][k]
						maxi = max(maxi, (2*min(x2, x)+y))
	print(maxi)	
	#for i in alph:
	#	print(i)
	#print()
