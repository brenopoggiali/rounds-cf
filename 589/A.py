a, b = map(int, input().split())

cant = True
while(a <= b):
	used = {}
	cant = False
	for i in str(a):
		if i not in used:
			used[i] = True
		else:
			cant = True
			break
	if not cant:
		break
	else:
		a += 1

if not cant:
	print(a)
else:
	print(-1)
