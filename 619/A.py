t = int(input())

for _ in range(t):
	s1 = input()
	s2 = input()
	s3 = input()
	
	can = True
	for i in range(len(s3)):
		if s1[i] == s3[i] or s2[i] == s3[i]:
			continue
		else:
			can = False
			break
	if can:
		print("YES")
	else:
		print("NO")
