from sys import exit

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	a, b, p = iis()
	s = input()
	old_s = s
	s = s[::-1][1:]
	count = 0
	last = s[0]
	first = s[0]
	if first == 'B':
		count += b
	else:
		count += a
	if count > p:
		print(len(s)+1)
		continue
	i = 0
	for i, c in enumerate(s):
		if last == c: continue
		if c == 'B':
			if count+b <= p:
				count += b
			else:
				break
		else:
			if count+a <= p:
				count += a
			else:
				break
		last = c
	
	
	if len(s)-i != 0:
		print(len(s)-i)
	else:
		print(len(s)-i)
