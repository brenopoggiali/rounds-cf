from sys import exit

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	bla = []
	s = input()
	last = 'R'
	count = 0
	for i in range(len(s)):
		if s[i] == 'L' and last == s[i]:
			count += 1
		elif s[i] == 'L':
			count = 1
		else:
			bla.append(count)
			count = 0
		last = s[i]
	bla.append(count)
	#print(bla)
	print(max(bla)+1)
