from sys import exit

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

def get_mx_pl(s):
	s += ' '
	for i in range(1, len(s)):
		s2 = s[:-(i)]
		if s2 == s2[::-1]:
			return s2
	return ""

def get_mx_pl_r(s):
	for i in range(len(s)):
		s2 = s[i:]
		if s2 == s2[::-1]:
			return s2
	return ""
	

t = ii()
for _ in range(t):
	s = input()
	pre, suf = "", ""
	i = 0
	while (i < len(s)//2 and s[i] == s[len(s)-1-i]):
		pre += s[i]
		suf += s[len(s)-1-i]
		i += 1
	pre2 = get_mx_pl(s[i:len(s)-len(suf)])
	suf2 = get_mx_pl_r(s[len(pre):len(s)-len(suf)])
	if (len(pre2) >= len(suf2)):
		pre += pre2
	else:
		suf += suf2
	print(pre + suf[::-1])
