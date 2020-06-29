from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	n, k = iis()	
	a = liis()
	need = set()
	hashe = {}
	for i in a:
		jose = i%k
		if jose != 0:
			nome = k-jose
			if nome not in hashe:
				need.add(nome)
				hashe[nome] = nome
			else:
				need.add(hashe[nome]+k)
				hashe[nome] += k
	if len(need):
		print(max(need)+1)
	else:
		print(0)
