from sys import exit

def i(): return input()
def lis(): return list(input().split())
def iis(): return map(int, input().split())
def ii(): return int(input())
def liis():	return list(map(int, input().split()))


n, k = iis()
s = i()
a = lis()
ans = n*(n+1)//2

ans = 0
tam = 0
for i in s:
	if i in a:
		tam += 1
	else:
		ans += tam*(tam+1)//2
		tam = 0

ans += tam*(tam+1)//2
print(ans)


