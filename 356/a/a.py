from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

def print_ans(a):
	for i in ans[1:]:
		if not len(i):
			print(0, end=" ")
		else:
			print(i[0], end=" ")	
	print()


n, m = iis()	
ans = [[] for i in range(n+1)]

for _ in range(m):
	l, r, x = iis()
	i = l
	j = set()
	while i <= r:
		#print(ans[i], '\t', ans)
		if len(ans[i]):
			if r >= ans[i][0] and x != ans[i][0] and len(ans[ans[i][0]]) == 0:
				ans[ans[i][0]] = [x, r]
			j.add(i)
			i  = ans[i][1]
			if len(ans[i]): 
				ans[i][1] = r
		elif i != x:
				ans[i] = [x, r]
		i += 1
	for i in j:
		#print(ans)
		ans[i][1] = r


print_ans(ans)
