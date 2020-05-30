t1 = int(input())

for _ in range(t1):
	n = int(input())
	s = input()
	t = input()
	can = False
	diff = 0
	diffs = []
	for i in range(len(s)):
		if s[i] != t[i]:
			diff += 1
			diffs.append(i)

	if diff == 2:
		first, sec = diffs[0], diffs[1]
		ss = []
		ss.append(s[:first] + t[sec] + s[first+1:])
		ss.append(s[:sec] + t[first] + s[sec+1:])
		ts = []
		ts.append(t[:first] + s[sec] + t[first+1:])
		ts.append(t[:sec] + s[first] + t[sec+1:])
		for i in ss:
			if i in ts:
				can = True
				break
	
	if can: print("Yes")
	else: print("No")
