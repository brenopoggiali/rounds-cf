from collections import deque

t = int(input())

for _ in range(t):
	n = int(input())
	s = input()
	pos = {(0, 0): -1}
	mini = float("INF")
	x = y = 0
	ans = []
	for i, c in enumerate(s):
		if c == 'L': x -= 1
		elif c == 'R': x += 1
		elif c == 'D': y -= 1
		elif c == 'U': y += 1
		if (x, y) in pos:
			if i-pos[(x,y)] < mini:
				ans = [pos[(x, y)], i]
				mini = i-pos[(x, y)]
		pos[(x, y)] = i
	
	if len(ans):
		print(ans[0]+2, ans[1]+1)
	else:
		print(-1)
