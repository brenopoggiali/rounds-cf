from sys import exit

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

n = ii()
s = input()

alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alph = alph[::-1]
count = 0
for c in alph:
	for j in range(n):
		for i in range(len(s)):
			if s[i] == c:
				if (i > 0 and ord(s[i-1]) == ord(s[i])-1) or (i < len(s)-1 and ord(s[i+1]) == ord(s[i])-1):
					s = s[:i] + s[i+1:]
					count += 1
					break
print(count)
