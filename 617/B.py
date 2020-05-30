t = int(input())
for _ in range(t):
	s = int(input())
	count = 0
	for i in range(1000):
		count += s//10
		s = s%10 + s//10
	print(int(str(count)+str(s)))

