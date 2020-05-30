from sys import exit

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

def power_of_two():
	pt = [[1]]
	for i in range(1, 1000):
		pt.append([2**i])
		for j in pt[-2]:
			pt[-1].append(j+2**i)
	return pt

t = ii()
pt = power_of_two()
#print(pt)
for _ in range(t):
	n = ii()
	a = liis()
	maxi = 0
	for i in range(1, n):
		if a[i] >= a[i-1]:
				continue
		for j in range(len(pt)):
			bola = False
			for k in range(len(pt[j])):
				if a[i]+pt[j][k] >= a[i-1]:
					a[i] += pt[j][k]
					maxi = max(maxi, j+1)
					bola = True
					break
			if bola:
				break
	print(maxi)

