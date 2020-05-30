t = int(input())

for _ in range(t):
	n = int(input())
	#min_l, min_r = map(int, input().split())
	inters = [float("INF"), 0]
	for i in range(n):
		l, r = map(int, input().split())
		if l <= inters[1] and r >= inters[0]:
			continue
		if l > inters[1]:
			inters[1] = l
			min_r = l
		if r < inters[0]:
			inters[0] = r
			min_l = r
		#print(inters)
	if inters[0] != float("INF"):
		if (inters[1]-inters[0]) < 0:
			print(0)
		else:
			print(inters[1]-inters[0])
	else:
		print(0)
