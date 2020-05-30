n, m = map(int, input().split())

a = []
for _ in range(n):
	s = input()
	a.append(s)

def is_palindrome(s1, s2):
	eh = True
	for i in range(len(s1)):
		if s1[i] != s2[m-i-1]:
			eh = False
			break
	return eh

def is_palindrome_alone(s1):
	eh = True
	for i in range(len(s1)):
		if s1[i] != s1[m-i-1]:
			eh = False
			break
	return eh

together = []
for i in range(len(a)):
	for j in range(i+1, len(a)):
		if a[i] != -1 and a[j] != -1 and is_palindrome(a[i], a[j]):
			together.append([a[i], a[j]])
			a[i] = -1
			a[j] = -1

alone = []
for i, s in enumerate(a):
	if s != -1 and is_palindrome_alone(s):
		alone.append(s)
		a[i] = -1
		break
stack = []
ans = []
for i in together:
	ans.append(i[0])
	stack.append(i[1])

for i in alone:
	ans.append(i)

while len(stack):
	ans.append(stack.pop())

ans = "".join(ans)
print(len(ans))
print(ans)
