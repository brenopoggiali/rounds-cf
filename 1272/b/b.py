from sys import exit

def iis(): return map(int, input().split())
def ii(): return int(input())
def liis():	return list(map(int, input().split()))

def get(s):
	u = s.count('U')	
	d = s.count('D')
	l = s.count('L')
	r = s.count('R')
	ans = ""
	if min(l, r) >= 1:
		ans = 'LR'
	if min(u, d) >= 1:
		ans = 'UD'
	if min(u, d) >= 1 and min(l, r) >= 1:
		minx = min(l, r)	
		miny = min(u, d)
		ans = minx*'L' + miny*'U' + minx*'R' + miny * 'D'
	return ans

t = ii()
for _ in range(t):
	s = input()
	ans = get(s)
	print(len(ans))
	print(ans)
exit(0)
