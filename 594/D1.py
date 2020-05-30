n = int(input())
s = input()
change = 0
count = 0
counts = []
can = True
direct = True
for index, i in enumerate(s):
	if count < -1:
		can = False
		break
	elif count < 0:
		direct = False
	if i == ")":
		count -= 1
	elif i == "(":
		count += 1
	if count < 0:
		first = index
	counts.append(count)


for index, j in enumerate(s[::-1]):
	if j == ")":
		count += 1
	elif j == "(":
		count -= 1
	if count < 0:
		second = n-index-1

if not can or n%2 != 0:
	print(0)
	print(1, 1)
elif direct and change == 0:
	ans = 0 
	for i in counts:
		if i == 1: ans += 1
	print(ans)
	print(1, 1)
else:
	s = s[:first] + s[second] + s[first+1:second-1] + s[first] + s[second+1:]
	ans = 0
	count = 0
	for i in s:
		if i == "(":
			count += 1
		elif i == ")":
			count -= 1
			if count == 0: ans += 1
	print(ans)
	print(first+1, second+1)

