from math import ceil

t = int(input())

def get_ans(n, r, p, s, bob, st):
	ans = [0]*n
	for i, value in enumerate(st):
		if value == "P":
			if s > 0:
				ans[i] = "S"
				s -= 1
		elif value == "S":
			if r > 0:
				ans[i] = "R"
				r -= 1
		elif value == "R":
			if p > 0:
				ans[i] = "P"
				p -= 1
	for i, value in enumerate(ans):
		if value == 0:
			if s > 0:
				s-= 1
				ans[i] = "S"
			elif r > 0:
				r-=1
				ans[i] = "R"
			elif p>0:
				p-=1
				ans[i] = "P"
	return "".join(ans)

for _ in range(t):
	n = int(input())
	r, p, s = map(int, input().split())
	st = input()
	bob = {"S":0, "R":0, "P":0}
	for i in st:
		bob[i] += 1
	need = ceil(n/2)
	alice_win = min(bob["P"], s) + min(bob["S"], r) + min(bob["R"], p)
	if alice_win < need:
		print("NO")
	else:
		print("YES")
		ans = get_ans(n, r, p, s, bob, st)
		print(ans)
