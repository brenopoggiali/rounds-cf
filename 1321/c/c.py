def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis(): return list(map(int, input().split()))

n = int(input())
s = input()
a = []

for i in range(len(s)):
	a.append(s[i])

a = sorted(a)[::-1]

count = 0
todos = set()
for c in a:
	for j in range(n):
		for i in range(len(s)):
			if s[i] == c and ((i > 0 and ord(s[i-1]) == ord(s[i])-1) or (i < len(s)-1 and ord(s[i+1]) == ord(s[i])-1)):
				s = s[:i] + s[i+1:]
#				print(s, i)
				count += 1
				break

print(count)
