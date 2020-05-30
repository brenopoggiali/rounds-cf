from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print("".join(map(str, a)))

def count_sets(final):
	sets = 0
	for i in final:
		if isinstance(i, set):
			sets += 1
	return sets


def count(strings, ans):
	for stri in strings:
		counter = 0
		for i, c in enumerate(stri):
			if ans[i] == c:
				continue
			else:
				counter += 1
		if counter > 1:
			return False
	return True

t = ii()
for _ in range(t):
	n, m = iis()	
	strings = []
	final = [set() for i in range(m)]
	for i in range(n):
		new = input().strip()
		strings.append(new)
		for idx, j in enumerate(new):
			final[idx].add(j)
	for idx, i in enumerate(final):
		if len(i) == 1:
			final[idx] = list(i)[0]
	can = False
	sets =  count_sets(final)
	la = 1
	print(final)
	if sets > 2:
		can = False
	else:
		if sets == 1:
			for idx, i in enumerate(final):
				if isinstance(i, set):
					final[idx] = list(i)[0]
					can = True
					break
		elif sets == 0:
			can = True
		else:
			idxs = []
			for idx, i in enumerate(final):
				if isinstance(i, set):
					idxs.append(idx)
					final[idx] = list(i)
			one, two = idxs[0], idxs[1]
			for i in range(len(final[one])):
				for j in range(len(final[two])):
					final2 = final[:]
					final2[one] = final[one][i]
					final2[two] = final[two][j]
					new_str = "".join(final2)
					c = count(strings, new_str)
					if c == True:
						la = 2
						can = True
						break
				if la == 2:
					break
	print(final)	
	if can:
		if la == 2:
			print(new_str)
		else:
			print_array(final)
	else:
		print(-1)
