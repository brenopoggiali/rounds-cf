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
#	print(s)
	s = s[:-1]
	if not len(s):
		print(1)
		continue
	last = s[0]
	count = 0
	if last == 'A': count += a
	else: count += b
	
	for c in s:
		if c == last: continue
		if c == 'A':
			count += a
		else:
			count += b
#		print(c, count)
		last = c
#	print(s, count)	
	i = 0
	first = count
	while (count > p and i < len(s)):
#		print(i, s[i])
		if i != 0 and s[i] == last: 
			i += 1
			continue
		last = s[i]
		if last == 'A':
			count -= a
		else:
			count -= b
		i += 1
	if first == count:
		print(i+1)
	else:
		while i > 0 and i < len(s) and s[i] == s[i-1]:
			i += 1
		print(i+1)
