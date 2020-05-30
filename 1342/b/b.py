from sys import stdin, exit
from collections import Counter
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print("".join(map(str, a)), end="")

t = ii()
for _ in range(t):
	s = input()	
	c = Counter(s)
	if len(c) == 2:
		print(s, end="")
		continue
	else:
		last = s[0]
		ans = [s[0]]
		for i in s[1:]:
			if i == '1':
				if ans[-1] == '0':
					ans.append(i)
				else:
					ans.append('0')
					ans.append(i)
			else:
				if ans[-1] == '0':
					ans.append('1')
					ans.append(i)
				else:
					ans.append(i)
		print_array(ans)
