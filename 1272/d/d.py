from sys import exit

def iis(): return map(int, input().split())
def ii(): return int(input())
def liis():	return list(map(int, input().split()))

n = ii()
a = liis()

fim = [0]*n
fim[0] = 1
tam = 1
for i in range(1, n):
	if a[i] <= a[i-1]:
		tam = 1
		fim[i] = tam
	else:
		fim[i] = tam+1
		tam += 1

cont = [0]*n
cont[n-1] = 1
tam = 1
for i in range(n-2, -1, -1):
	if a[i] >= a[i+1]:
		tam = 1
		cont[i] = tam
	else:
		cont[i] = tam+1
		tam += 1

ans = 0
for i in range(n): ans = max(ans, cont[i])
for i in range(1, n-1): 
	if a[i-1] < a[i+1]:
		ans = max(ans, fim[i-1]+cont[i+1])
print(ans)
