from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	n, x, m = iis()
	ranges = [[x, x]]
	for i in range(m):
		l, r = iis()
		for j in ranges:
			if l <= j[1] and r >= j[0]:
				ranges.append([l, r])
				break
	final_ans = []
	for r in ranges:
		can = True
		for r2 in final_ans:
			if r[1] >= r2[1] and r[0] <= r2[1]:
				r2[1] = r[1]
				can = False
			if r[0] <= r2[0] and r[1] >= r2[0]:
				r2[0] = r[0]
				can = False
			if r[0] >= r2[0] and r[1] <= r2[1]:
				can = False
			if not can:
				break
		if can:
			final_ans.append(r)
	count = 0
	for i in final_ans:
		count += max(i)-min(i)+1
	print(count)
