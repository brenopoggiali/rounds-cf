from sys import exit
from collections import Counter

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

t = ii()
for _ in range(t):
	n = ii()
	a = liis()
	jose = Counter(a)
	cur = 0
	for i in range(1, n):
		if i not in jose:
			break
		if jose[i] == 2:
			cur += 1
		else:
			break

	maxi = cur
	for i in range(cur+1, n):
		if i in jose:
			maxi += 1
		else:
			break
	
	
	first = [i for i in range(1, cur+1)]
	final = [i for i in range(1, maxi+1)]
	first_set = set(first)
	final_first_set = set(final)
	second_set = set(first)
	final_second_set = set(final)

	possible = 0
	ans = []
	can = True
	for i in range(len(first)):
		if a[i] in first_set:
			first_set.remove(a[i])
		else:
			can = False
			break
	for i in range(len(final)):
		if a[len(a)-i-1] in final_first_set:
			final_first_set.remove(a[len(a)-i-1])
		else:
			can = False
			break
	if can and not len(first_set) and not len(final_first_set):
		#print("primeito", final_first_set, first_set, first, final)
		possible += 1
		ans.append([len(first), n-len(first)])

	can = True
	for i in range(len(first)):
		if a[len(a)-i-1] in second_set:
			second_set.remove(a[len(a)-i-1])
		else:
			can = False
			break
	for i in range(len(final)):
		if a[i] in final_second_set:
			final_second_set.remove(a[i])
		else:
			can = False
			break
	
	if can and not len(final_second_set) and not len(second_set):
		#print("segundo")
		possible += 1
		ans.append([n-len(first), len(first)])

	if len(ans) == 2 and ans[0] == ans[1]:
		ans.pop()
	
	if possible and len(final)+len(first) == n:
		print(len(ans))
		for i in ans:
			print(i[0], i[1])

	else:
		print(0)

