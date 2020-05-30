from math import ceil

n, a, b, k = map(int, input().split())
h = list(map(int, input().split()))

sobra = []
for i in range(len(h)):
	aux = h[i]
	mod = aux%(a+b)
	if mod == 0: # B ganha cravado, então fazemos B jogar uma a menos.
		aux = ceil(b/a)
	elif mod <= a: # A ganha direto, sem precisar gastar nada.
		aux = 0
	else: # Ninguem ganha cravado, mas eh a vez do A jogar.
		aux = ceil((mod-a)/a)
	sobra.append(aux)

sobra = sorted(sobra)
count = 0
for i in sobra:
	if i <= k:
		count += 1
		k -= i
	else:
		break
print(count)

