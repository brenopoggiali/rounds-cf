t = int(input())

for _ in range(t):
	n = int(input())
	perm = list(map(int, input().split()))
	ans = [str(0)]*len(perm)
	my_dict = {}
	have_ans = True
	poss = [i for i in range(len(perm), 0, -1)]
	
	s = sorted(perm)
	for i in range(len(s)):
		if i >= s[i]: 
			have_ans = False
			break
	
	if have_ans:
		biggest_available = len(perm)
		for i, v in enumerate(perm):
			if v not in my_dict:
				my_dict[v] = 1
				ans[i] = str(v)
			else:
				v = biggest_available
				while (v in my_dict):
					v -= 1
					if v < 1:
						break
				if v < 1:
					have_ans = False
					break
				ans[i] = str(v)
				my_dict[v] = 1
			if v == biggest_available:
				while (biggest_available in my_dict):
					biggest_available -= 1
	
	if not have_ans:
		print(-1)
	else:
		print(" ".join(ans))
