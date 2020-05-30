from sys import exit

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

n, m = iis()
l = liis()
ans = []
soma = sum(l)
if soma < n or max(l)-1 > m:
	print(-1)
else:
	i = 0
	new_l = []
	for idx, i in enumrate(l):
		new_l.append([i, idx])
	l = sorted(l)[::-1]
	ans = [0 for i in range(m)]
	i = 
	for idx, li in l:
		soma -= li
		p = n-li+1
		ans.append(p-i)
		i += 1

	print_array(ans)
