from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

def calcular(a):
	soma = 0
	for idx, i in enumerate(a[:-1]):
		soma += abs(a[idx]-a[idx+1])
		
	return soma


t = ii()
for _ in range(t):
	n = ii()	
	p = liis()
	a = p[0]
	numbers1 = [a]
	numbers2 = [a]
	last = p[0]
	cresce = True
	for i in p[1:]:
		if cresce:
			if i >= last:
				last = i
			else:
				numbers1.append(last)
				last = i
				cresce = False
		else:
			if i <= last:
				last = i
			elif numbers1[-1] != last:
				#print(numbers1, last, i)
				numbers1.append(last)
				last = i
				cresce = True
	
	cresce = False
	last = p[0]
	for i in p[1:]:
		if cresce:
			if i >= last:
				last = i
			else:
				numbers2.append(last)
				last = i
				cresce = False
		else:
			if i <= last:
				last = i
			elif last != numbers2[-1]:
				numbers2.append(last)
				last = i
				cresce = True

	if numbers1[-1] != p[-1]: numbers1.append(p[-1])
	if numbers2[-1] != p[-1]: numbers2.append(p[-1])

	#print('n1', numbers1)
	#print('n2', numbers2)


	if calcular(numbers1) > calcular(numbers2):
		print(len(numbers1))
		print_array(numbers1)
	elif calcular(numbers1) == calcular(numbers2):
		if len(numbers1) < len(numbers2):
			print(len(numbers1))
			print_array(numbers1)
		else:
			print(len(numbers2))
			print_array(numbers2)
	else:
		print(len(numbers2))
		print_array(numbers2)

