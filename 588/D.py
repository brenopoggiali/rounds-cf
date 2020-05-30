n = int(input())
a = list(map(bin, map(int, input().split())))
b = list(map(int, input().split()))

skills = [[]]*(n)

for i in range(n):
	binary = a[i][2:][::-1]
	for j in range(len(binary)):
		if binary[j] == '1':
			skills[i] = skills[i][:] + [j]

print(skills)

max_ = []
for i in range(len(skills)):
	can = False
	sum_ = b[i]
	for j in range(len(skills)):
		if i == j:
			continue
		elif skills[i] == skills[j]:
			sum_ += b[j]
			can = True
		elif all(k in skills[i] for k in skills[j]):
			sum_ += b[j]
	if can:
		max_.append(sum_)

print(max_)

if len(max_) != 0:
	print(max(max_))
else:
	print(0)
