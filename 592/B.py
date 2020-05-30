t = int(input())
for i in range(t):
	n = int(input())
	s = input()
	if int(s) > int(s[::-1]):
		s = s[::-1]
	count = 0
	last_one = -1
	count_one = 0
	chance = n
	for i, j in enumerate(s):
		if j == '1':
			last_one = i+1
			chance += 1
	print(max([last_one*2, n, chance]))
