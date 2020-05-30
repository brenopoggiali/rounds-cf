h, w = map(int, input().split())
r = list(map(int, input().split()))
c = list(map(int, input().split()))

squares = h*w
known = 0
possible = True
for i in range(h):
	known += r[i]
	if r[i] != w:
		known += 1
	for j in range(r[i]):
		if c[j] == i:
			possible = False
			break
for i in range(w):
	known += c[i]
	aux = 0
	if c[i] != h:
		known += 1
		aux = 1
	for j in range(c[i]):
		if r[j] == i:
			possible = False
			break
	for j in range(c[i]+aux):
		if r[j] >= i:
			known -= 1

if possible:
	print(2**(squares-known)%1000000007)
else: 
	print(0)
