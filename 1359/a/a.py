from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	n, m, k = iis()	
	venc = min(n//k, m)
	m -= venc
	resto = m//(k-1)
	if m%(k-1) != 0:
		resto += 1
	print(venc-resto)
