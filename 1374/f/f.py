from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a+1)))

def change(a, i):
	a[i], a[i+1], a[i+2] = a[i+2], a[i], a[i+1]
	return a

def colocar(a, idx, lugar):
	if idx-lugar == 0:
		return a
	if idx-lugar == 1:
		change(a, idx-1)
		indices.append(idx-1)
		change(a, idx-1)
		idx -= 1
	else:
		change(a, idx-2)
		idx -= 2
	indices.append(idx)
	colocar(a, idx, lugar)

def jose():
	print('a', a)
	opa = indices[:]
	for i in range(len(indices)):
		opa[i] += 1
	print('i', opa)


t = ii()
for _ in range(t):
	n = ii()	
	a = liis()
	indices = []
	numbers = {}
	for i in a: 
		if i not in numbers:
			numbers[i] = 0
		numbers[i] += 1
	sort = sorted(a)
	fixos = 0
	for i in range(501):
		if i in numbers:
			if fixos >= n-2: break
			while numbers[i] > 0:
				if fixos >= n-2: break
				for idx in range(fixos, n):
					if a[idx] == i and idx != fixos:
						colocar(a, idx, fixos)
						#jose()
						break
				numbers[i] -= 1
				fixos += 1
	print(a)
	if a == sort:
		print(len(indices))
		for i in indices:
			print(i+1, end=" ")
		print()
	else:
		print(-1)
