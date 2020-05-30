n, k = map(int, input().split())

s = input()

k_aux = 0
i = 0
if i == 0 and k > 0:
	if s[i] == '1':
		i += 1
	else:
		s =  s[:i] + '1' + s[i+1:]
		k_aux += 1
		i += 1
while i < n and k_aux < k:
	if k-k_aux >= n-i:
		s = s[:i] + '0'*(n-i)
		i += n-i
		k_aux += n-i
		continue
	elif s[i] == '0':
		i += 1
		continue
	else:
		s = s[:i] + '0' + s[i+1:]
		k_aux += 1
	i += 1

if n == 1 and k > 0:
	print(0)
else:
	print(s)
