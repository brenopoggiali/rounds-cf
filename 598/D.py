q = int(input())

for _ in range(q):
	n, k = map(int, input().split())
	s = input()
	arr = []
	for i in s:
		arr.append(int(i))
	ones = set()
	zeros = set()
	for i in range(len(arr)):
		if arr[i] == 1:
			ones.add(i)
		else:
			zeros.add(i)
	if len(zeros):
		sm = min(zeros)
	else:
		sm = k+1
	count = 0
	while(sm-count <= k):
		zeros.discard(sm)
		k -= (sm-count)
		count += 1
		if len(zeros):
			sm = min(zeros)
		else:
			break
	if len(zeros) and k > 0:
		zeros.discard(sm)
		sm -= k
	else:
		sm = n+1
	ans = ["0"]*n
	for ind, i in enumerate(ans):
		if ind >= count and ind not in zeros and ind != sm:
			ans[ind] = "1"
	print("".join(ans))
	
